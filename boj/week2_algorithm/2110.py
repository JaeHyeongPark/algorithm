# N: 집 개수, C: 공유기 개수
import sys
N, C = map(int, sys.stdin.readline().split(" "))
houses = []
for i in range(N):
    houses.append(int(sys.stdin.readline()))

houses.sort()
answer = 0

def findOptimalDist(start, end, arr):
    while start <= end:
        mid = (start + end)//2
        current = arr[0]
        count = 1
        for i in range(1, len(arr)):
            if arr[i] >= current + mid:
                count += 1
                current = arr[i]
        if count >= C:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

start = 1
end = houses[-1] - houses[0]
findOptimalDist(start, end, houses)
print(answer)