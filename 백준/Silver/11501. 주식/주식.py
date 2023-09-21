import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))
    answer = 0
    max_v = 0

    for i in range(n-1, -1, -1):
        if prices[i] > max_v:
            max_v = prices[i]
        else:
            answer += max_v - prices[i]

    print(answer)