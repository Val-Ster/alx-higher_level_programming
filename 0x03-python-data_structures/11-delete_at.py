#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if idx is negative or out of range
if idx < 0 or idx >= len(my_list):
    return my_list # Return the same list without changes
# Remove the item at the specified index using list slicing
del my_list[idx]
return my_list
