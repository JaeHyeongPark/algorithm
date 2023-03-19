import sys
import heapq

N = int(sys.stdin.readline()) # 1 ~ 100,000
decks= []
for _ in range(N):
    heapq.heappush(decks, int(sys.stdin.readline()))
answer = 0
while len(decks) > 1:
    deck1 = heapq.heappop(decks)
    deck2 = heapq.heappop(decks)
    answer += (deck1 + deck2)
    heapq.heappush(decks, (deck1+deck2))

print(answer)