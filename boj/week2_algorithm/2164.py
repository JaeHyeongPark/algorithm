import sys
from collections import deque

N = int(sys.stdin.readline())
tmp = [i for i in range(1, N+1)]
q = deque(tmp)

while len(q) > 1:
    q.popleft()
    a = q.popleft()
    q.append(a)

print(q.popleft())
