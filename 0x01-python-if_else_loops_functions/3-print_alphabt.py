#!/usr/bin/python3

exempted_letters = ['e', 'q']
output = ""

for ascii_value in range(97, 123):
    char = chr(ascii_value)
    if char not in exempted_letters:
        output += char

print(f"{output}", end=' ')

