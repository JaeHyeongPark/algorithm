#핵심 아이디어: 9원짜리로 20원을 만들 때, 11원을 만드나, 20원을 만드나, 달라지는 건 9원이 1개만 추가된다는 사실.

import sys
#T; test case; 1~10
T = int(sys.stdin.readline().strip())
for _ in range(T):
    #N: variety of coins
    N = int(sys.stdin.readline().strip())
    #coins: N coins with ascending order; 1~10,000
    coins = []
    coins = list(map(int,sys.stdin.readline().strip().split()))
    #M: target
    M = int(sys.stdin.readline().strip())
    dp = [0]*(M+1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, M+1):
            dp[i] = dp[i] + dp[i-coin]
    print(dp[M])

