#!/usr/bin/python3
def element_at(my_list, idx):
    # Check if idx is negative

    if idx < 0 or idx >= len(my_list):
        # it alows bothi.e if i use just d if<0 nd if i use d if nd d or >=
        return None
    # Initialize a variable to keep track of the current index
    current_idx = 0
    # Iterate through the list
    for element in my_list:
        # If the current index matches the desired index, return the element
        if current_idx == idx:
            return element
        current_idx += 1
        # If idx is out of range, return None
        return none
