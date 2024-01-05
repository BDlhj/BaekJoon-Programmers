import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, k, t, m = map(int, input().split())
    logs = [list(map(int, input().split())) for _ in range(m)]
    result = defaultdict(list)

    for i in range(n):
        submit_count = 0
        last_submit = 0
        scores = [0] * k

        for j in range(m):
            if logs[j][0] == i+1:
                submit_count += 1
                last_submit = j

                if scores[logs[j][1]-1] < logs[j][2]:
                    scores[logs[j][1]-1] = logs[j][2]

        result[i].append(sum(scores))
        result[i].append(-submit_count)
        result[i].append(-last_submit)

    final_result = list(result.items())
    final_result.sort(key=lambda x: (x[1]), reverse=True)
    
    answer = 0
    for i in range(n):
        if final_result[i][0]+1 == t:
            answer = i+1
            
    print(answer)