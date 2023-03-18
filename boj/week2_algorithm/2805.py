import sys
# M : 가져가야 하는 길이
N, M = map(int, sys.stdin.readline().split(" "))
trees = list(map(int, sys.stdin.readline().split(" ")))
trees.sort()

maxH = max(trees)

#어떤 것을 start, end 로 넣을지 고민해야됨
def findOptimalH(start, end, arr):
    while (end - start) >= 0:
        mid = (start + end)//2
        height_sum = 0
        for tree in trees:
            if tree > mid:
                height_sum += tree-mid
        if height_sum >= M:
            start = mid+1
        else:
            end = mid-1
    return (end)

print(findOptimalH(0, maxH, trees))