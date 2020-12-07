#!/usr/bin/env python3

import re

def bags_can_contain(bag, rule_list):
    pattern = r'(^.+ bag)s? contain .+ ' + bag
    for rule in rule_list:
        match = re.search(pattern, rule)
        if match:
            print(match.group(1), "can contain", bag)
            if match.group(1) not in can_contain:
                can_contain.append(match.group(1))
                print("(Not in list, appended)")

input = open('input', 'r').read().splitlines()

can_contain = []

bags_can_contain('shiny gold bag', input)

for bag in can_contain:
    bags_can_contain(bag, input)

print(len(can_contain), "bags can contain shiny gold bag")
