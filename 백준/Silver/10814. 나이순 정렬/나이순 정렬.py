import sys
input = sys.stdin.readline

n = int(input())
members = [input().split() for _ in range(n)]

for member in members:
    member[0] = int(member[0])
members.sort(key=lambda x: x[0])

for member in members:
    print(member[0], member[1])