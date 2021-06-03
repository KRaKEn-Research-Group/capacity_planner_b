import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ortools.constraint_solver import pywrapcp
from historical_data_generation import matrix_generator
from historical_data_generation import demand_generator
from tools import time_generator
from ortools.constraint_solver import routing_enums_pb2


n = 20
def create_data_model():
    """Stores the data for the problem."""
    data = {}
    time_matrix = matrix_generator.generate_time_matrix("data/in/nodes.json", n)

    data['time_matrix'] = time_matrix
    data['time_windows'] = time_generator.generate_time_windows(n)
    data['num_vehicles'] = n
    data['depot'] = 0
    data['demands'] = demand_generator.demand_for_shops(1).T[0][0:n+1] #???
    data['demands'][0]=0                    #THIS NEEDS TO BE FIXED
    data['vehicle_capacities'] = np.ones((1,n), np.int64)[0]*max(data['demands'])

    return data


data = create_data_model()
# print(data['time_windows'])
# print(data['time_matrix'])
manager = pywrapcp.RoutingIndexManager(len(data['time_matrix']), data['num_vehicles'], data['depot'])
routing = pywrapcp.RoutingModel(manager)

###

def time_callback(from_index, to_index):
    """Returns the travel time between the two nodes."""
    # Convert from routing variable Index to time matrix NodeIndex.
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return data['time_matrix'][from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(time_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

###


time = 'Time'
routing.AddDimension(
    transit_callback_index,
    7*6,  # allow waiting time
    23*6,  # maximum time per vehicle
    False,  # Don't force start cumul to zero.
    time)
time_dimension = routing.GetDimensionOrDie(time)
for i in range(n):
    time_dimension.SetSpanUpperBoundForVehicle(9*6, i)
# Add time window constraints for each location except depot.
for location_idx, time_window in enumerate(data['time_windows']):
    if location_idx == data['depot']:
        continue
    index = manager.NodeToIndex(location_idx)
    time_dimension.CumulVar(index).SetRange(time_window[0], time_window[1])


# Add time window constraints for each vehicle start node.
depot_idx = data['depot']
for vehicle_id in range(data['num_vehicles']):
    index = routing.Start(vehicle_id)
    time_dimension.CumulVar(index).SetRange(
        data['time_windows'][depot_idx][0],
        data['time_windows'][depot_idx][1])
for i in range(data['num_vehicles']):
    routing.AddVariableMinimizedByFinalizer(
        time_dimension.CumulVar(routing.Start(i)))
    routing.AddVariableMinimizedByFinalizer(
        time_dimension.CumulVar(routing.End(i)))


###

def demand_callback(from_index):
    """Returns the demand of the node."""
    # Convert from routing variable Index to demands NodeIndex.
    from_node = manager.IndexToNode(from_index)
    return data['demands'][from_node]

demand_callback_index = routing.RegisterUnaryTransitCallback(
    demand_callback)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index,
    0,  # null capacity slack
    data['vehicle_capacities'],  # vehicle maximum capacities
    True,  # start cumul to zero
    'Capacity')

###

def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    print(f'Objective: {solution.ObjectiveValue()}')
    time_dimension = routing.GetDimensionOrDie('Time')
    total_time = 0
    total_distance = 0
    total_load = 0
    needed_vehicles = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(needed_vehicles+1)
        route_load = 0
        while not routing.IsEnd(index):
            time_var = time_dimension.CumulVar(index)
            node_index = manager.IndexToNode(index)
            route_load += data['demands'][node_index]
            plan_output += '\tNode: {0:3}\tDemand: {1:2}\t'.format(node_index, data['demands'][node_index])
            plan_output += 'Time: {0:3} - {1:3}\t\tOpen hours: {2:3} - {3:3}\n'.format(
                solution.Min(time_var),
                solution.Max(time_var),
                data['time_windows'][node_index][0],
                data['time_windows'][node_index][1])
            previous_index = index
            index = solution.Value(routing.NextVar(index))
        time_var = time_dimension.CumulVar(index)
        plan_output += '\tNode: {0:3}\tDemand: {1:2}\t'.format(manager.IndexToNode(index), data['demands'][manager.IndexToNode(index)])
        plan_output += 'Time: {0:3} - {1:3}\t\tOpen hours: {2:3} - {3:3}\n'.format(manager.IndexToNode(index),
                                                    solution.Min(time_var),
                                                    solution.Max(time_var),
                                                    data['time_windows'][0][1], #???
                                                    data['time_windows'][0][0])
        plan_output += 'Load of the route: {}\n'.format(route_load)
        plan_output += 'Time of the route: {}\n'.format(
            solution.Min(time_var))
        if(solution.Min(time_var)==0):
            continue
        print(plan_output)
        needed_vehicles += 1
        total_time += solution.Min(time_var)
        total_load += route_load
    print('=============================================')
    print('Vehicles needed: {}'.format(needed_vehicles))
    print('Total time of all routes: {}'.format(total_time))
    print('Total load of all routes: {}'.format(total_load))
    print('=============================================')

for i in range(data['num_vehicles']):
    routing.AddVariableMinimizedByFinalizer(
        time_dimension.CumulVar(routing.Start(i)))
    routing.AddVariableMinimizedByFinalizer(
        time_dimension.CumulVar(routing.End(i)))

search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
search_parameters.time_limit.FromSeconds(1)

solution = routing.SolveWithParameters(search_parameters)

if solution:
    print_solution(data, manager, routing, solution)
else:
    print('No solution found !')
