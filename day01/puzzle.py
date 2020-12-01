#!/usr/bin/env python3

input = open('input', 'r').read().split()

for i in input:
    if str(2020-int(i)) in input:
        print("Number pair:", i, 2020-int(i))
        print("Answer 1:", int(i)*(2020-int(i)))
        break

for i in input:
    for j in input:
        if str(2020-int(i)-int(j)) in input:
            print("Number pair:", i, j, 2020-int(i)-int(j))
            print("Answer 2:", int(i)*int(j)*(2020-int(i)-int(j)))
            break
