import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
negative = []
zero = []
positive = []
answer = 0

for num in nums:
    if num > 0:
        positive.append(num)
    if num < 0:
        negative.append(num)
    if num == 0:
        zero.append(num)

positive.sort(reverse=True)
negative.sort()

if len(positive) > 1:
    for i in range(1, len(positive), 2):
        if positive[i] != 1 and positive[i-1] != 1:
            answer += positive[i] * positive[i-1]
        else:
            answer += (positive[i] + positive[i-1])
    if len(positive) % 2 == 1:
        answer += positive[-1]
elif len(positive) == 1:
    answer += positive[0]

if len(negative) > 1:
    for i in range(1, len(negative), 2):
        answer += negative[i] * negative[i-1]
    if len(negative) % 2 == 1:
        if not zero:
            answer += negative[-1]
elif len(negative) == 1:
    if not zero:
        answer += negative[-1]

print(answer)