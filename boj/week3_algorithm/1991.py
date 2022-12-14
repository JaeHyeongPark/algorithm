import sys

N = int(sys.stdin.readline().strip())
graph = {}
stack = []

for _ in range(N):
    node_info = list(sys.stdin.readline().strip().split(" "))
    root = node_info[0]
    left = node_info[1] if node_info[1] != '.' else 0
    right = node_info[2] if node_info[2] != '.' else 0
    graph[root] = [left, right]

def preorder(graph, start):
    stack.append(start)
    left = graph[start][0]
    right = graph[start][1]
    if left != 0:
        preorder(graph, left)
    if right != 0:
        preorder(graph, right)

def inorder(graph, start):
    left = graph[start][0]
    right = graph[start][1]
    if left != 0:
        inorder(graph, left)
        stack.append(start)
    else:
        stack.append(start)
    if right != 0:
        inorder(graph, right)

def postorder(graph, start):
    left = graph[start][0]
    right = graph[start][1]
    if left != 0:
        postorder(graph, left)
    if right != 0:
        postorder(graph, right)
    stack.append(start)

preorder(graph, 'A')
for i in range(len(stack)):
    print(stack[i], end='')
print()
stack =[]
inorder(graph, 'A')
for i in range(len(stack)):
    print(stack[i], end='')
print()
stack =[]
postorder(graph, 'A')
for i in range(len(stack)):
    print(stack[i], end='')