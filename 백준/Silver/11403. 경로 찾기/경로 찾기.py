import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(num):
    for j in range(n):
        if graph[num][j] and not visited[j]:
            visited[j] = 1
            dfs(j)

visited = [0] * n
for i in range(n):
    dfs(i)
    print(' '.join(map(str, visited)))
    visited = [0] * n