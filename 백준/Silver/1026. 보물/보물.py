n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b_reversed = sorted(b, reverse=True)

answer = map(lambda x, y: x * y, a, b_reversed)

print(sum(answer))