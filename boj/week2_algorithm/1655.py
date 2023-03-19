import sys
import heapq
#최소힙

N = int(sys.stdin.readline()) # 1<= <=100,000

leftHeap = []
rightHeap = []
# answer = []

for i in range(N):
    integer = int(sys.stdin.readline()) # -10,000 ~ 10,000
    
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -integer)
    else:
        heapq.heappush(rightHeap, integer)
    
    if rightHeap and (-leftHeap[0] > rightHeap[0]):
        leftVal = -heapq.heappop(leftHeap)
        rightVal = heapq.heappop(rightHeap)
        heapq.heappush(leftHeap, -rightVal)
        heapq.heappush(rightHeap, leftVal)
    print(-leftHeap[0])
        

