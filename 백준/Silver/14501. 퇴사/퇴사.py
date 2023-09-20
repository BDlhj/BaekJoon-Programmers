import sys
input = sys.stdin.readline

n = int(input())
infos = []
pay = [0]
d = [0] * 16

for i in range(n):
    t, p = map(int, input().split())
    infos.append((i+1, i+t, p))
    pay.append(p)
infos.sort(key=lambda x: (x[1], -x[0]))

for info in infos:
    if info[1] > n:
        continue
        
    if info[0] == info[1]:
        d[info[1]] = max(d[:info[0]]) + pay[info[1]]

    else:
        d[info[1]] = max(max(d[:info[0]]) + pay[info[0]], max(d[info[0]:info[1]]), d[info[1]])

print(max(d))