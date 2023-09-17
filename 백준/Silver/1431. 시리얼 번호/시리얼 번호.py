import sys
input = sys.stdin.readline

def add(li):
    answer = 0
    for i in li:
        if i.isdigit():
            answer += int(i)
    return answer

n = int(input())
serials = [list(input().rstrip()) for _ in range(n)]
serials.sort(key=lambda x: (len(x), add(x), x))

for serial in serials:
    print(''.join(serial))
