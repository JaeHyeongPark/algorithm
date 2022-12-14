import sys

tree = {}
sys.setrecursionlimit(10**4)

def postorder(tree, start):
    if start == False or tree=={}:
        return
    postorder(tree, tree[start][0])
    postorder(tree, tree[start][1])
    print(start)

while True:
    try:
        num = int(sys.stdin.readline().strip())
        if tree == {}:
            tree[num] = [False, False] #left, right
            root = num
        else:
            current = root
            while True:
                if num > current:
                    if tree[current][1] == False:
                        tree[current][1] = num
                        tree[num] = [False, False]
                        break
                    else:
                        current = tree[current][1]
                else:
                    if tree[current][0] == False: #왼쪽 자식이 없다면
                        tree[current][0] = num
                        tree[num] = [False,False]
                        break
                    else:
                        current = tree[current][0]
    except:
        if tree=={}:
            root = False
        break

postorder(tree, root)