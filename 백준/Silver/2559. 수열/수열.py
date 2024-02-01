import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temperatures = list(map(int, input().split()))
if n == k:
    print(sum(temperatures))
else:
    sub_max = sum(temperatures[:k])
    answer = sub_max
    for end_idx in range(k, n):
        sub_max += (temperatures[end_idx] - temperatures[end_idx-k])
        answer = max(answer, sub_max)

    print(answer)