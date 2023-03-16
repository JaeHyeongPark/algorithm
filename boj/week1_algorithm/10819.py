# N : 정수 개수
# A : 숫자 배열
import sys
from itertools import permutations 

N = int(sys.stdin.readline()) # 3 ~ 8
inputNums = list(map(int, sys.stdin.readline().split(" "))) # -100 ~ 100

permut = list(permutations(inputNums))
result = []

def calArray(lis):
    result = 0
    for i in range(len(lis)-1):
        result += abs(lis[i]-lis[i+1])
    return result

for perm in permut:
    res = calArray(perm)
    result.append(res)

print(max(result))
