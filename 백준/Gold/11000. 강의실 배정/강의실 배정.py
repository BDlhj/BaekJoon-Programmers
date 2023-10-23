import sys
import heapq
input = sys.stdin.readline

n = int(input())
timetable = [list(map(int, input().split())) for _ in range(n)]
timetable.sort()
classroom = []

for lecture in timetable:
    s, t = lecture[0], lecture[1]
    if not classroom:
        heapq.heappush(classroom, t)
        continue
    if classroom[0] > s:
        heapq.heappush(classroom, t)
    else:
        heapq.heappop(classroom)
        heapq.heappush(classroom, t)

print(len(classroom))