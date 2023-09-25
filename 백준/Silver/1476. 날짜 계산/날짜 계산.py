import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())

for i in range(1, 10000):
    if i % 15 == e % 15 and i % 28 == s % 28 and i % 19 == m % 19:
        print(i)
        break