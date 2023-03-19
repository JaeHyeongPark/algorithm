# 시간초과 발생 -> 스택에서 탑을 제거하는 방식 채택
import sys
N = int(input())
tops = list(map(int, sys.stdin.readline().split(" ")))

stk = []
result = []

for i in range(0, len(tops)):
    # i번째 탑 vs 미리 저장해둔 탑들
    flag = True
    while stk:
        if tops[i] >= stk[-1][1]:
            stk.pop()
        else:
            result.append(stk[-1][0])
            stk.append((i+1, tops[i])) #index, 탑 크기
            flag = False
            break
    if flag:
        stk.append((i+1, tops[i]))
        result.append(0)

print(*result)