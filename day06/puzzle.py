#!/usr/bin/env python3

import re
import string

input = open('input', 'r').read().split('\n\n')

anyone_yes = 0
everyone_yes = 0

for group in input:
    group_anyone_yes = 0
    group_everyone_yes = 0
    persons = len(group.splitlines())
    group = group.replace('\n', '')
    for i in string.ascii_lowercase:
        group_matches = re.findall(i, group)
        if group_matches:
            group_anyone_yes += 1
            anyone_yes += 1
        if len(group_matches) == persons:
            group_everyone_yes += 1
            everyone_yes += 1
    print("Group", group, "anyone", group_anyone_yes)
    print("Group", group, "everyone", group_everyone_yes)

print("All anyone yes:", anyone_yes)
print("All everyone yes:", everyone_yes)
