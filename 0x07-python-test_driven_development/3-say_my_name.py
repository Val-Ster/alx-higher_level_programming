#!/usr/bin/python3
"""Prints 'My name is <first name> <last name>'
"""


def say_my_name(first_name, last_name=""):

    """ Prints 'My name is <first name> <last name>' to stdout.

        Args:
        first_name(str) : the first name of the user
        last_name(str, optional) : last name of user, has a default " " value.
    """
    if type(first_name) not in (str,):
        # could have also used if type(last_name) not == str: if i wanted to
        raise TypeError("first_name must be a string")

    if not first_name:
        raise ValueError("first_name can't be empty string")

    if type(last_name) not in (str,):
        # could have also used if type(last_name) not == str: if i wanted to
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name.strip()} {last_name.strip()}")
