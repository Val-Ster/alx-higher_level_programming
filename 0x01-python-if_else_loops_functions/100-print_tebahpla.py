#!/usr/bin/python3
for i in range(ord('z'), ord('A') - 1, -1):
    if i % 2 == 0:
        letter = chr(i)
    else:
        letter = chr(i).upper()
    print("{}".format(letter), end='')
