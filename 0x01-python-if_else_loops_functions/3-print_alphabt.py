#!/usr/bin/python3

exempted_letters = ['e', 'q']

for ascii_value in range(97, 123):
    char = chr(ascii_value)
    if char not in exempted_letters:
        print(char, end=' ')
