#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Initialize an empty list to store the results
    result = []
    # Iterate through the original list
    for num in my_list:
        # Check if the integer is divisible by 2
        is_divisible = num % 2 == 0
        result.append(is_divisible)
        return result
