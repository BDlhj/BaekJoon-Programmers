n = int(input())

for _ in range(n):
    first, second = input().split()
    if sorted(first) == sorted(second):
        print('Possible')
    else:
        print('Impossible')