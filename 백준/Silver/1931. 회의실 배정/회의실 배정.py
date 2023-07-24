num_of_meetings = int(input())
times = []
end_time = -1
count = 0

for _ in range(num_of_meetings):
    times.append(tuple(map(int, input().split())))

times.sort(key=lambda x: (x[1], x[0]))

for i in times:
    if i[0] >= end_time:
        count += 1
        end_time = i[1]

print(count)