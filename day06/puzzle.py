#!/usr/bin/env python3

import re
import string

input = open('input', 'r').read().split('\n\n')

yes_count = 0

for group in input:
    group_yes = 0
    group = group.replace('\n', '')
    for i in string.ascii_lowercase:
        if re.search(i, group):
            group_yes += 1
            yes_count += 1
    print("Group", group, group_yes)

print("All yes:", yes_count)
