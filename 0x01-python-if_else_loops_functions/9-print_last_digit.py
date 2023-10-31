#!/usr/bin/python3
def print_last_digit(number):
    # Ensure the number is positive for the last digit calculation
    if number < 0:
        number = -number

    # Get the last digit using modulo operator
    last_digit = number % 10

    # Print the last digit
    print(last_digit, end='')

    # Return the last digit as an integer
    return last_digit

# Test cases
 if __name__ == "__main__":
    print_last_digit(98)
    print_last_digit(0)
    r = print_last_digit(-1024)
    print(r)
