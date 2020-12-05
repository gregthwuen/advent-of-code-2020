#!/usr/bin/env python3

input = open('input', 'r').read().splitlines()

id_list = []

for seat in input:
    row_range = list(range(0, 128))
    column_range = list(range(0, 8))
    for i in range(0, len(seat)):
        if seat[i] == 'F':
            row_range = row_range[:len(row_range) // 2]
        if seat[i] == 'B':
            row_range = row_range[len(row_range) // 2:]
        if seat[i] == 'L':
            column_range = column_range[:len(column_range) // 2]
        if seat[i] == 'R':
            column_range = column_range[len(column_range) // 2:]
    seat_id = row_range[0] * 8 + column_range[0]
    id_list.append(seat_id)
    print("Seat", seat + ": row", row_range[0], "column", column_range[0])
    print("Seat ID:", seat_id)

print("Highest seat ID:", max(id_list))
