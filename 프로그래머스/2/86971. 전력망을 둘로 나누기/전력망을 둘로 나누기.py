def dfs(graph, visited, r, group):
    if not visited[r]:
        visited[r] = True
        group.append(r)
        for i in range(len(graph[r])):
            if not visited[i] and graph[r][i]:
                dfs(graph, visited, i, group)
    
def solution(n, wires):
    answer = []
    
    for i in range(n - 1):
        graph = [[0] * (n + 1) for _ in range(n + 1)]
        visited = [False] * (n + 1)
        group = []
        
        for j in range(n - 1):
            if i != j:
                graph[wires[j][0]][wires[j][1]] = 1
                graph[wires[j][1]][wires[j][0]] = 1
        
        for r in range(1, n + 1):
            for c in range(1, n + 1):
                if graph[r][c] == 1:
                    dfs(graph, visited, r, group)
                    if group:
                        break
            if group:
                break
                
        count = len(group)
        answer.append(abs(count - (n - count)))

    return min(answer)