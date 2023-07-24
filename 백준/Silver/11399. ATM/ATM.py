people_num = int(input())
waiting_times = list(map(int, input().split()))

answer = 0

waiting_times.sort(reverse=True)
for i, j in enumerate(waiting_times):
    answer += ((i+1) * j)

print(answer)