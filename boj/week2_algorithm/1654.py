# K : 랜선개수, N : 필요한 랜선 개수
import sys

K, N = map(int, sys.stdin.readline().split(" "))
lineList = []
for i in range(K):
    lineList.append(int(sys.stdin.readline()))
lineList.sort()

start = 1
end = lineList[-1]
answer = 0

while start <= end:
    mid = (start + end)//2
    count = 0
    for line in lineList:
        count += (line // mid)
    if count >= N:
        # answer = start
        start = mid + 1
    else:
        end = mid - 1

# print(start)
print(end)