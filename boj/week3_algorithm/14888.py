import sys

# N <= 11
N = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().strip().split()))
numPlus, numSub, numMul, numDev = map(int, sys.stdin.readline().split())

#연산자를 숫자로 치환?
maximum = -10**9
minimum = 10**9

def dfs(count, ans, numPlus, numSub, numMul, numDev):
    global maximum, minimum
    if count == N-1:
        maximum = max( maximum, ans )
        minimum = min( minimum, ans )
        return

    if numPlus > 0:
        dfs(count+1, ans+num_list[count+1], numPlus-1, numSub, numMul, numDev)
    if numSub > 0:
        dfs(count+1, ans-num_list[count+1], numPlus, numSub-1, numMul, numDev)
    if numMul > 0:
        dfs(count+1, ans*num_list[count+1], numPlus, numSub, numMul-1, numDev)
    if numDev > 0:
        if ans < 0:
            dfs(count+1, -(abs(ans)//num_list[count+1]), numPlus, numSub, numMul, numDev-1)
        else:
            dfs(count+1, ans//num_list[count+1], numPlus, numSub, numMul, numDev-1)

dfs(0, num_list[0], numPlus, numSub, numMul, numDev)
print(maximum)
print(minimum)