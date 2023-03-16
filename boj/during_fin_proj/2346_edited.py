# N : 1~1000
import sys
from collections import deque

N = int(sys.stdin.readline().strip())
number = [0] + list(map(int, sys.stdin.readline().split()))
balloons = [(i, number[i]) for i in range(1, N+1)]
q = deque(balloons)
result = []

while q:
    a = q.popleft()
    num_of_balloon = a[0]
    balloon_num = a[1]
    if (balloon_num < 0):
        q.rotate(-balloon_num)
    else:
        q.rotate(-balloon_num+1)
    result.append(a[0])

print(*result)