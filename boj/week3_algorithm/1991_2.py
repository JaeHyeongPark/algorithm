import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

N = int(input())
tr = {} ##dict로 트리 설정
for _ in range(N):
    root,left,right = input().rstrip().split()
    tr[root] = [left,right]

def preorder(root):
    if root !='.':
        print(root, end='')
        preorder(tr[root][0])
        preorder(tr[root][1])
def inorder(root):
    if root !='.':
        inorder(tr[root][0])
        print(root,end='')
        inorder(tr[root][1])
def postorder(root):
    if root !='.':
        postorder(tr[root][0])
        postorder(tr[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')