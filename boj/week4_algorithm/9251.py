import sys

character_1 = [0]+list(sys.stdin.readline().strip())
character_2 = [0]+list(sys.stdin.readline().strip())

dp = [[0 for _ in range(len(character_2))] for _ in range(len(character_1))]

for i in range(1, len(character_1)):
    for j in range(1, len(character_2)):
        if character_1[i] == character_2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(character_1)-1][len(character_2)-1])