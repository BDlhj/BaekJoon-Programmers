import sys
import heapq
input = sys.stdin.readline

N = int(input())
prob_infos = sorted([list(map(int, input().split())) for _ in range(N)])
cup_noodles_gained = []

for prob in prob_infos:
    heapq.heappush(cup_noodles_gained, prob[1])
    if prob[0] < len(cup_noodles_gained):
        heapq.heappop(cup_noodles_gained)

print(sum(cup_noodles_gained))