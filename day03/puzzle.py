#!/usr/bin/env python3

input = open('input', 'r').read().splitlines()

column = 0
abs_column = 0
trees = 0

for i in input:
    if column >= len(i):
        column -= len(i) 
    if i[column] == '#':
        trees += 1
        print(i, "tree at column", abs_column)
    else:
        print(i)
    column += 3
    abs_column += 3

print("Encountered trees:", trees)
