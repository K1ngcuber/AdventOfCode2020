import math

seatings = []
max_id = 0

row_start = 0
row_end = 127
row_mid = row_end / 2

col_start = 0
col_end = 7
col_mid = col_end / 2

with open("door5_input.txt",'r') as f:
    seatings = list(f.readlines())

for line in seatings:
    row_index = line[:7]
    col_index = line[7::]
    for letter in row_index:
        if letter == 'F':
            row_end = math.floor(row_mid)
            
        elif letter == 'B':
            row_start = math.ceil(row_mid)
        
        row_mid = row_start + (row_end-row_start)/2
    
    for letter in col_index:
        if letter == "L":
            col_end = math.floor(col_mid)
        elif letter == "R":
            col_start = math.ceil(col_mid)

        col_mid = col_start + (col_end-col_start)/2

    if row_start * 8 + col_start > max_id:
        max_id = row_start * 8 + col_start

    row_start = 0
    row_end = 127
    row_mid = row_end / 2

    col_start = 0
    col_end = 7
    col_mid = col_end / 2

print(max_id)