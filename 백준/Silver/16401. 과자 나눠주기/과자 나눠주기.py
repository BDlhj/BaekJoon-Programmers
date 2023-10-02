import sys
input = sys.stdin.readline

m, n = map(int, input().split())
lengths = list(map(int, input().split()))

def parametric_search():
    start, end = 1, int(10e8)
    answer = 0

    while start <= end:
        nums = 0
        mid = (start + end) // 2
        for length in lengths:
            nums += length // mid
        if nums < m:
            end = mid - 1
        if nums >= m:
            start = mid + 1
            answer = mid
    return answer

print(parametric_search())
