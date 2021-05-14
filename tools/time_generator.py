import random

# depot too?
def generate_time_windows(n):
    list_of_ranges = []

    for i in range(n//2):
        rand_val = random.randint(5,9) # 5:00 - 9:00
        rand_period = random.randint(1,3) # 1h-3h
        list_of_ranges.append((rand_val,rand_val+rand_period))

    # how to do 23:00 - 02:00?
    for i in range(n//2, n):
        rand_val = random.randint(19,23) # 19:00 - 23:00
        rand_period = random.randint(1,3) # 1h-3h
        if rand_val + rand_period > 24:
            rand_period -= (rand_val + rand_period - 24)
        list_of_ranges.append((rand_val,rand_val+rand_period))
    random.shuffle(list_of_ranges)
    list_of_ranges.insert(0,(0,5))
    return list_of_ranges
