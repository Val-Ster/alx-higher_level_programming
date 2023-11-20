#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        x = [1, 2, 3, 4, 5]
        for i in range (x)
        print (list[i], end="")
    except IndexError:
        print("List index out of range")
