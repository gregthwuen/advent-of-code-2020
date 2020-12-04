#!/usr/bin/env python3

import re

input = open('input', 'r').read()

input = list(filter(None, re.split(r'\n| |: |-', input)))
# creates a usable list out of input string

input = [input[i:i + 4] for i in range(0, len(input), 4)]
# groups elements in lists to sublists

valid_pws_p1 = 0

for i in input:
    if int(i[0]) <= i[3].count(i[2]) <= int(i[1]):
        valid_pws_p1 += 1
        print("Found valid pw (puzzle 1):", i[3])

valid_pws_p2 = 0

for i in input:
    if (i[3][int(i[0]) - 1] == i[2]) != (i[3][int(i[1]) - 1] == i[2]):
        valid_pws_p2 += 1
        print("Found valid pw (puzzle 2):", i[3])

print("Valid passwords (puzzle 1):", valid_pws_p1)
print("Vaild passwords (puzzle 2):", valid_pws_p2)
