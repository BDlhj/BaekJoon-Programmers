def dfs(computers, visited, i):
    visited[i] = True
    for idx, is_connected in enumerate(computers[i]):
        if is_connected and not visited[idx]:
            dfs(computers, visited, idx)


def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            answer += 1
    
    return answer