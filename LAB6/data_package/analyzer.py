import math
def calculate_mean(num_list):
    i = 0
    for num in num_list:
        i += num
    return i / len(num_list)

def find_maximum(num_list):
    max = 0
    for num in num_list:
        if num > max:
            max = num
    return max

def find_minimum(num_list):
    min = math.inf
    for num in num_list:
        if num < min:
            min = num
    return min