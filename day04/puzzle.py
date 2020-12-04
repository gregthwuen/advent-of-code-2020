#!/usr/bin/env python3

import re

input = open('input', 'r').read().strip().split('\n\n')

for i in range(0, len(input)):
    input[i] = re.split('\n| ', input[i])

fields_needed = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
valid_passports = 0

for passport in input:
    valid_fields = 0
    for field in passport:
        for i in fields_needed:
            if re.match(i, field):
                valid_fields += 1
    if valid_fields == 7:
        valid_passports += 1
        print("Passport valid", passport)
    else:
        print("Passport invalid", passport)

print("Valid passports:", valid_passports)
