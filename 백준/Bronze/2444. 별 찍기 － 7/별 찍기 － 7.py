n = int(input())

for i in range(1, n*2):
    if i < n+1:
        print(' ' * (n-i) + '*' * (2*i-1))
    else:
        print(' ' * (i-n) + '*' * (2*(2*n-i)-1))