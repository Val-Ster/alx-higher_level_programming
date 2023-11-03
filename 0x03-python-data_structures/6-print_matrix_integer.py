#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            # Use str.format() to print integers with appropriate formatting
            if i == len(row) - 1:
                # No space after the last element in each row
                print("{:d}".format(num), end="")
            else:
                # Space after each element except the last one
                print("{:d} ".format(num), end="")
                print()
