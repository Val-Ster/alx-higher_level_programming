#!/usr/bin/python3
def remove_char_at(s, n):
    if n < 0 or n >= len(s):
        return s  # If n is out of bounds, return the original string
    else:
        new_str = ""
        for i in range(len(s)):
            if i != n:
                new_str += s[i]
        return new_str
