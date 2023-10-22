import sys
input = sys.stdin.readline

n = int(input())
crane_capabilities = list(map(int, input().split()))
m = int(input())
box_weights = list(map(int, input().split()))

crane_capabilities.sort(reverse=True)
box_weights.sort(reverse=True)

if crane_capabilities[0] < box_weights[0]:
    print(-1)
else:
    answer = 0
    while box_weights:
        for i in range(len(crane_capabilities)):
            for j in range(len(box_weights)):
                if crane_capabilities[i] >= box_weights[j]:
                    del box_weights[j]
                    break
        answer += 1

    print(answer)