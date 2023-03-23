# N : 1~50 남극에 있는 단어 개수
# K : 0~26 가르치는 단어 개수(a~z)
# 단어길이: 8~15
# a, n, t, i , c : 5개
import sys
from itertools import combinations
N, K = map(int, sys.stdin.readline().split(" "))

ord_map = [0 for i in range(27)]
for word in ['a','n','t','i','c']:
    ord_map[ord(word)-97] = 1

# print(ord('a')) - 97~0
# print(ord('n')) - 110~13
# print(ord('t')) - 116~19
# print(ord('i')) - 105~8
# print(ord('c')) - 99~2

ord_list = [i for i in range(27)]
ord_list.remove(0)
ord_list.remove(2)
ord_list.remove(13)
ord_list.remove(8)
ord_list.remove(19)

word_list = []
for i in range(N):
    word_list.append(sys.stdin.readline().strip()[4:-4])

# print(word_list)

answer = 0

if K < 5:
    print(0)
else:
    for order in list(combinations(ord_list, K-5)):
        for idx in order:
            ord_map[idx] = 1
        count = 0
        for word in word_list:
            flag = True
            for string in word:
                if ord_map[ord(string)-97] == 0:
                    flag = False
                    break
            if flag:
                count += 1
        answer = max(answer, count)
        for idx in order:
            ord_map[idx] = 0
    print(answer)

