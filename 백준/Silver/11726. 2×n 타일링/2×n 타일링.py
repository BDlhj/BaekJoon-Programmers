import sys
input = sys.stdin.readline

def memo(d, n):
    if n <= 2:
        return d[n]
    
    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]
    
    return d[-1]

# 2 X n
n = int(input())

# d[i] : 2 X i 크기의 직사각형을 채우는 경우의 수
d = [0] * (n+1)
d[1] = 1

if n > 1:
    d[2] = 2

result = memo(d, n)

print(result % 10007)