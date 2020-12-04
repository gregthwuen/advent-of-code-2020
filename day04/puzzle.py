#!/usr/bin/env python3

import re

def check_passports(regex, fields_req, pp_list):
    import re
    print("Checking list...")
    valid_passports = 0
    for passport in pp_list:
        valid_fields = 0
        for field in passport:
            if re.match(regex, field):
                valid_fields += 1
        if valid_fields >= fields_req:
            valid_passports += 1
            print("Passport valid", passport)
        else:
            print("Passport invalid", passport)
    return valid_passports

input = open('input', 'r').read().strip().split('\n\n')

for i in range(0, len(input)):
    input[i] = re.split('\n| ', input[i])

are_passports = check_passports('byr|iyr|eyr|hgt|hcl|ecl|pid', 7, input)

valid_passports = check_passports('byr:(19[2-9][0-9]|200[0-2])$'
    '|iyr:20(1[0-9]|20)$'
    '|eyr:20(2[0-9]|30)$'
    '|hgt:(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)$'
    r'|hcl:#([0-9]|[a-f]){6}$'
    '|ecl:(amb|blu|brn|gry|grn|hzl|oth)$'
    r'|pid:[0-9]{9}$',
    7,
    input)

print("Are passports:", are_passports)
print("Valid passports:", valid_passports)
