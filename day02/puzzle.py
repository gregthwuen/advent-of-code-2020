#!/usr/bin/env python3

import re

input = open('input', 'r').read()

input = list(filter(None, re.split(r'\n| |: |-', input)))

input = [input[i:i + 4] for i in range(0, len(input), 4)]

correct_pws = 0

for i in input:
    if int(i[0]) <= i[3].count(i[2]) <= int(i[1]):
        correct_pws += 1
        print("Found valid pw:", i[3])

print("Valid passwords:", correct_pws)
