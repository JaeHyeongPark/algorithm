import itertools
import sys

def print_cnt(n) :
    cnt = 0
    result = []
    middle = []

    for i in range(n+1) :
        temp1 = 1 * i
        for j in range(0, (n//2)+1, 1) :
            temp2 = 2 * j
            for k in range(0, (n//3)+1, 1) :
                temp3 = 3 * k
                if temp1 + temp2 + temp3 == n : 
                    result.append([i, j, k])
                    print(result)

    for i in result :
        temp = []
        for j in range(i[0]) :
            temp.append(1)
        for j in range(i[1]) :
            temp.append(2)
        for j in range(i[2]) :
            temp.append(3)
        middle.append(temp)

    for i in middle :
        temp = list(itertools.permutations(i, len(i)))
        temp = list(set(temp))
        cnt += len(temp)

    return cnt

n = int(sys.stdin.readline())
value = []
for i in range(n) :
    value.append(int(sys.stdin.readline()))

for i in range(n) :
    print(print_cnt(value[i]))