import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lengths = list(map(int, input().split()))

def parametric_search():
    start, end = 0, int(10e8)
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        l = 0
        
        for length in lengths:
            if length > mid:
                l += length - mid
            
        if l >= m:
            start = mid + 1
            answer = mid
        if l < m:
            end = mid - 1

    return answer

print(parametric_search())