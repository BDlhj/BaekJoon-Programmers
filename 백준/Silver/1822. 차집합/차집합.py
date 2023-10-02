import sys
input = sys.stdin.readline

def binary_search(num):
    start, end = 0, m-1
    
    while start <= end:
        mid = (start + end) // 2
        if b[mid] == num:
            return True
        if b[mid] > num:
            end = mid - 1
        if b[mid] < num:
            start = mid + 1
    return False

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
answer = []

for num in a:
    if not binary_search(num):
        answer.append(str(num))

print(len(answer))
if answer:
    print(' '.join(answer))