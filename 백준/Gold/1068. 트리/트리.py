import sys
input = sys.stdin.readline

def delete(node):
    for child in node:
        if not deleted[child]:
            deleted[child] = True
            delete(children[child])

N = int(input())

children = [[] for _ in range(N)]

parents = list(map(int, input().split()))
node_to_delete = int(input())
deleted =[False] * N
num_of_leaf_nodes = 0

for i in range(N):
    for j in range(N):
        if parents[j] == i:
            children[i].append(j)

for i in range(N):
    if i == node_to_delete:
        deleted[i] = True
        delete(children[i])

for i in range(N):
    if not deleted[i]:
        if node_to_delete in children[i]:
            children[i].remove(node_to_delete)
        if len(children[i]) == 0:
            num_of_leaf_nodes += 1

print(num_of_leaf_nodes)
