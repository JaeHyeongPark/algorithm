import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for i in range(N):
    command = int(sys.stdin.readline())
    if command == 0:
        if heap == []:
            print(0)
        else:
            print(-1 * heapq.heappop(heap))
    else:
        heapq.heappush(heap, -command)