#!/usr/bin/python3

my_list=[1,'cat',3,'mouse',5,8,]
x=0

def print_list(list,X):
    try:
        num_of_ele=0
        for x in list:
            print(x)
            num_of_ele=num_of_ele+1
            print("number",num_of_ele)
    except IndexError:
        print('invalid')

print_list(my_list,x)
