import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    d = [0] * 101
    d[1], d[2], d[3], d[4], d[5] = 1, 1, 1, 2, 2
    
    if n <= 5:
        print(d[n])
        continue

    for i in range(6, n+1):
        d[i] = d[i-1] + d[i-5]
    
    print(d[n])