import sys
from itertools import combinations

a = list(sys.stdin.readline().strip().split())
N = int(a[0])
S = int(a[1])

test_case = list(map(int, sys.stdin.readline().strip().split()))
# 합이 S가 되는 부분 수열 개수 출력
print(test_case)
count = 0

for i in range(1, N+1):
    #원소가 1개인거부터 N개인거 까지
    for j in combinations(test_case, i):
        if sum(j) == S:
            count+=1

print(count)