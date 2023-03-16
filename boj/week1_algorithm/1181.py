#길이가 짧은 것부터
#길이가 같으면 사전 순으로
import sys
N = int(sys.stdin.readline()) # 1 ~ 20,000
wordList = [[] for _ in range(51)]

for _ in range(N):
    word = sys.stdin.readline().strip()
    wordLen = len(word)

    if not (word in wordList[wordLen]):
        wordList[wordLen].append(word)

for i in range(51):
    if len(wordList[i]) != 0:
        wordList[i].sort()
        for j in wordList[i]:
            print(j)