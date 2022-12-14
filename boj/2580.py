import sys

sudoku_map = [[-1]] # padding horizontal line insert first
zero_pos = [] # gathers (x,y) position of '0'

for i in range(9):
    horizontal_line = [-1] + list(map(int, input().split(' ')))    
    sudoku_map.append(horizontal_line)
    if 0 in horizontal_line:
        zero_pos.append((i+1, horizontal_line.index(0)))

