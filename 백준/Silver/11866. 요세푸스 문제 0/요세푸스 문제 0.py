n, k = map(int, input().split())
left = [i+1 for i in range(n)]
dead = []
idx = k-1

while len(left) > 0:
    dead.append(left.pop(idx))
    idx += (k-1)
    while idx >= len(left) and len(left) >= 1:
        idx -= len(left)

answer = '<' + ', '.join(list(map(str, dead))) + '>'

print(answer)