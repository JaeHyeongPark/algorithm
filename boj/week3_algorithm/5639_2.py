import sys
sys.setrecursionlimit(10**4)
num_list=[]

while True:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break

def postorder(first, end):
    if first > end:
        return
    
    for i in range(first+1, end+1):
        if num_list[first] < num_list[i]:
            mid = i
            break
    else: mid = end + 1 #for-if-break-else
    postorder(first+1, mid-1)
    postorder(mid, end)
    print(num_list[first])

postorder(0, len(num_list)-1)
    
