import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
students = [input().rstrip() for _ in range(n)]
count_dict = defaultdict(int)
answer = 0

for i in students[1:k+1]:
    count_dict[len(i)] += 1

end_idx = k
for start_idx in range(n):
    answer += count_dict[len(students[start_idx])]
    end_idx += 1
    
    if end_idx < n:
        count_dict[len(students[end_idx])] += 1
    if start_idx + 1 < n:
        count_dict[len(students[start_idx+1])] -= 1
    
print(answer)
