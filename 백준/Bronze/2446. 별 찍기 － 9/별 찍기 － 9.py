n = int(input())
for i in range(1, n):
    print(' ' * (i-1) + '*' * (2*(n-i)+1))
for i in range(n, n*2):
    print(' ' * (2*n-i-1) + '*' * (2*(i-n)+1))