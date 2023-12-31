import sys
input = sys.stdin.readline

n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
idx = 0
price = prices[idx]
answer = 0

while idx < n-1:
    if price > prices[idx+1]:
        answer += price * distances[idx]
        idx += 1
        price = prices[idx]
    else:
        answer += price * distances[idx]
        idx += 1

print(answer)