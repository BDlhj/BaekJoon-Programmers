import sys
input = sys.stdin.readline

i = 0
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break

    i += 1
    answer = l * (v // p) + min((v % p), l)
    
    print(f'Case {i}: {answer}')
