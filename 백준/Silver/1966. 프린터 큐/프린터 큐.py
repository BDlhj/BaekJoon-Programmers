import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n, doc = map(int, input().split())
    weights = list(map(int, input().split()))
    doc_list = [(i, w) for i, w in enumerate(weights)]
    weights.sort()
    q = deque(doc_list)
    answer = 0

    while q:
        if q[0][1] >= weights[-1]:
            popped = q.popleft()
            weights.pop()
            answer += 1
            if popped[0] == doc:
                break
        else:
            q.append(q.popleft())
    
    print(answer)