import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
food_locations = []
eaten_food_num = 0
shark_size = 2
shark_location = 0
answer = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def food_exists(shark_size):
    global shark_location

    for row in range(n):
        for col in range(n):
            if 0 < graph[row][col] < shark_size:
                food_locations.append((row, col))
            if graph[row][col] == 9:
                shark_location = (row, col)

    if food_locations:
        return True
    return False

def bfs(shark_location, destination):
    q = deque()
    visited = [[0] * n for _ in range(n)]

    q.append(shark_location)
    visited[shark_location[0]][shark_location[1]] = 1

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if (0 <= ny < n and 0 <= nx < n) and graph[ny][nx] <= shark_size and not visited[ny][nx]:
                visited[ny][nx] = visited[cy][cx] + 1
                q.append((ny, nx))
                if (ny, nx) == (destination[0], destination[1]):
                    food_distances.append((visited[ny][nx]-1, ny, nx))

while food_exists(shark_size):
    food_distances = []
    for food_location in food_locations:
        bfs(shark_location, food_location)
        
    if not food_distances:
        break
        
    food_distances.sort(key=lambda x: (x[0], x[1], x[2]))
    answer += food_distances[0][0]
    graph[food_distances[0][1]][food_distances[0][2]] = 0
    graph[shark_location[0]][shark_location[1]] = 0
    shark_location = (food_distances[0][1], food_distances[0][2])
    
    eaten_food_num += 1
    if eaten_food_num == shark_size:
        shark_size += 1
        eaten_food_num = 0
    food_locations = []
    
print(answer)