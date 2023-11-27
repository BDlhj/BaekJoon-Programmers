import sys
input = sys.stdin.readline

n, m = map(int, input().split())
not_heard = set(input().rstrip() for _ in range(n))
not_seen = set(input().rstrip() for _ in range(m))

duplicated = list(not_heard & not_seen)
duplicated.sort()
print(len(duplicated))
print('\n'.join(duplicated))