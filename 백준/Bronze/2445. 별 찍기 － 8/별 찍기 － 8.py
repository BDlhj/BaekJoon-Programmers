n = int(input())
for i in range(1, n):
    print('*' * i + ' ' * (2*(n-i)) + '*' * i)
for i in range(n, n*2):
    print('*' * (2*n-i) + ' ' * (2*(i-n)) + '*' * (2*n-i))