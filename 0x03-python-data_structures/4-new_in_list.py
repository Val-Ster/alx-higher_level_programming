#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Check if idx is negative or out of range

    if idx < 0 or idx >= len(my_list):

        return my_list[:]  # Return a copy of the original list
    # Create a new list to store the modified elements

    new_list = []
    # Iterate thru d original list nd copy d elements with modification at idx
    for i in range(len(my_list)):
        if i == idx:
            new_list.append(element)  # Replace the element at idx
        else:
            new_list.append(my_list[i])
            return new_list
