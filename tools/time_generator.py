import random
import sys
import os
from tools import node_parser

# depot too?
# def generate_time_windows(n):
#     list_of_ranges = []

#     # for i in range(n):
#     #     rand_val = random.randint(0*60,23*60) # 19:00 - 23:00
#     #     rand_period = random.randint(1*60,7*60) # 1h-3h
#         # rand_val = 0
#         # rand_period = random.randint(1*60,23*60) # 19:00 - 23:00

#     #     if rand_val + rand_period > 24*60:
#     #         rand_period -= (rand_val + rand_period - 24*60)
#     #     list_of_ranges.append((rand_val,rand_val+rand_period))
#     # random.shuffle(list_of_ranges)

#     for i in range(n//2):
#         rand_val = random.randint(5*6,9*6) # 5:00 - 9:00
#         #rand_period = random.randint(1*6,3*6) # 1h-3h
#         rand_period = random.choice([1 * 6, 2*6, 3 * 6])  # 1h-3h
#         list_of_ranges.append((rand_val,rand_val+rand_period))

#     # how to do 23:00 - 02:00?
#     for i in range(n//2, n):
#         rand_val = random.randint(17*6,20*6) # 19:00 - 23:00
#         #rand_period = random.randint(1*6,3*6) # 1h-3h
#         rand_period = random.choice([1 * 6, 2 * 6, 3 * 6])  # 1h-3h
#         if rand_val + rand_period >= 24*6:
#             rand_period -= (rand_val + rand_period - 24*6)
#         list_of_ranges.append((rand_val,rand_val+rand_period))
#     random.shuffle(list_of_ranges)
#     list_of_ranges.insert(0, (0, 23*6+5))
#     print(list_of_ranges)
#     return list_of_ranges

def generate_time_windows(n):
    list_of_ranges = []
    list_of_ranges.append((0,144))

    node_data = node_parser.parse_node_parameters("data/out/node_parameters.txt")

    for node in node_data:
        if node[1] == "parking":
            list_of_ranges.append((24,144))
        else:
            rand_val = random.randint(24,96)
            list_of_ranges.append((rand_val,rand_val+6))
    return list_of_ranges[0:n+1]
