import sys
# 구멍개수 1~100
# total count K 1~100
N,K= map(int, sys.stdin.readline().strip().split())
using_order = list(map(int, sys.stdin.readline().strip().split()))

# consent = [0 for _ in range(K+1)]
# consent_size = 0

# consentBound=0

# for i in range(len(using_order)):
#     if sum(consent) < N:
#         consent[using_order[i]] == 1
#         continue        
#     elif consent[using_order[i]] == 1:
#         pass
#     else:
#         for j in range(len(consent)):
#             if consent[j] == 0:
#                 continue
#             if j+1 not in using_order[]
    
plugs = []
result = 0
for i in range(K):
    if using_order[i] in plugs:
        continue
    if len(plugs) != N:
        plugs.append(using_order[i])
        continue
    
    further_idx = 0
    tmp = 0

    for plug in plugs:
        if plug not in using_order[i:]:
            tmp = plug
            break
        elif using_order[i:].index(plug) > further_idx:
            further_idx = using_order[i:].index(plug)
            tmp = plug
    
    plugs[plugs.index(tmp)] = using_order[i]
    result += 1

print(result)