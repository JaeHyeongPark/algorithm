import sys

N = int(sys.stdin.readline().strip())
time_table = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().strip().split())
    time_table.append((start, end))

sorted_table = sorted(time_table, key = lambda x: (x[1], x[0]))
result_table = [(0,0)]
for time in sorted_table:
    if time[0] >= result_table[-1][1]:
        result_table.append(time)

print(len(result_table)-1)
