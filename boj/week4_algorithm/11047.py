#동전 N종류, 합을 K로.
#동전 개수 최소값.
import sys

N, K = map(int, sys.stdin.readline().strip().split())
wallet = []

for _ in range(N):
    coin = int(sys.stdin.readline().strip())
    if coin > K:
        continue
    wallet.append(coin)
#wallet은 오름차순임
cnt = 0

while True:
    if K == 0:
        break
    coin = wallet.pop()
    if K < coin:
        continue
    n = K // coin
    K -= coin * n
    cnt += n

print(cnt)