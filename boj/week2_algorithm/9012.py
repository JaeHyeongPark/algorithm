import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    paren_list = list(sys.stdin.readline().strip())
    stk = []
    for elem in paren_list:
        # if elem == '(':
        #     stk.append(elem)
        # else:
        #     if stk[-1] == '(':
        #         stk.pop()
        #     else:
        if elem == ')':
            if stk != []:
                if stk[-1] == '(':
                    stk.pop()
                    continue
        stk.append(elem)
    if stk == []:
        print("YES")
    else:
        print("NO")