import sys

N = int(sys.stdin.readline().strip())

rows=[False]
cols=[False]

for _ in range(N):
    r,c = map(int, sys.stdin.readline().strip().split())
    rows.append(r)
    cols.append(c)

memo = [[0 for _ in range(N+1)] for _ in range(N+1)]

mm = float('INF')

def calculateMatrixMultiple(x,y):
    if memo[x][y] > 0:
        return memo[x][y]
    global mm
    if (y-x) <=0:
        return 0
    for k in range(x, y):
        mm = min(mm, calculateMatrixMultiple(x,k) + calculateMatrixMultiple(k+1, y)+ rows[x]*cols[k]*cols[y])
        memo[x][y] = mm
    
    return memo[x][y]

print(calculateMatrixMultiple(1, N))