#!/usr/bin/env python3

import math

def slope_trees(map,r,d):
    column = 0
    abs_column = 0
    trees = 0
    print("Slope: right:", r, "down:", d)
    for i in map[0::d]:
        if column >= len(i):
            column -= len(i) 
        if i[column] == '#':
            trees += 1
            print(i, "at column", abs_column, "tree")
        else:
            print(i, "at column", abs_column)
        column += r
        abs_column += r
    print("Encoutered", trees, "trees with this slope")
    return trees

input = open('input', 'r').read().splitlines()

trees = []

trees.append(slope_trees(input,1,1))
trees.append(slope_trees(input,3,1))
trees.append(slope_trees(input,5,1))
trees.append(slope_trees(input,7,1))
trees.append(slope_trees(input,1,2))

print("Encountered trees:", trees)
print("Product of encountered trees:", math.prod(trees))
