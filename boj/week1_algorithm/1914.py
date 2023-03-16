import sys

K = int(sys.stdin.readline())

def hanoi(n:int, a:int, b:int, c:int):
    if(n==1):
        print(a, c, sep = " ")
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)

print(2**K-1)
if (K <= 20):
    hanoi(K, 1, 2, 3)