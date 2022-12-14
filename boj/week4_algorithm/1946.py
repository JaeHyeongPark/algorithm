import sys
#1~20
T = int(sys.stdin.readline().strip())
#1~100,000
for _ in range(T):
    participants = []
    N = int(sys.stdin.readline().strip())
    for _ in range(N):
        a,b = map(int, sys.stdin.readline().strip().split())
        participants.append((a,b))
    temp_list = sorted(participants, key = lambda x : (x[0], -x[1]))

    result = [temp_list[0]]
    for i in range(1, N):
        if result[-1][1] >= temp_list[i][1]:
            result.append(temp_list[i])

    print(len(result))