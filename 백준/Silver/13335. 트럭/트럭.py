import sys
from collections import deque
input = sys.stdin.readline

# 트럭 수, 다리 길이, 최대 하중
n, w, L = map(int, input().split())
weights = deque(map(int, input().split()))
trucks_on_bridge = deque() # 다리 위에 있는 트럭들의 무게를 담은 덱
truck_weights_sum_on_bridge = 0 # 다리 위에 있는 트럭들의 무게의 합
truck_idx = 0
truck_times = deque() # 다리 위에 있는 트럭들이 전진한 횟수
total_time = 0

while truck_idx < n:
    # 다리 위에 트럭이 있는 조건
    if trucks_on_bridge:
        # 다리 위에 있는 맨 앞의 트럭 내보내는 조건
        if truck_times[0] == w:
            truck_weights_sum_on_bridge -= trucks_on_bridge.popleft()
            truck_times.popleft()
            
            # 다리에 트럭을 더 추가할 수 있는 조건
            if truck_weights_sum_on_bridge + weights[truck_idx] <= L:
                trucks_on_bridge.append(weights[truck_idx])
                truck_weights_sum_on_bridge += weights[truck_idx]
                truck_times.append(0)
                for idx in range(len(truck_times)):
                    truck_times[idx] += 1
                truck_idx += 1

            # 다리에 트럭을 더 추가할 수 없는 조건
            else:
                for idx in range(len(truck_times)):
                    truck_times[idx] += 1
                
        # 내보낼 트럭이 없는 조건
        else:
            # 다리에 트럭을 더 추가할 수 있는 조건
            if truck_weights_sum_on_bridge + weights[truck_idx] <= L:
                trucks_on_bridge.append(weights[truck_idx])
                truck_weights_sum_on_bridge += weights[truck_idx]
                truck_times.append(0)
                for idx in range(len(truck_times)):
                    truck_times[idx] += 1
                truck_idx += 1

            # 다리에 트럭을 더 추가할 수 없는 조건
            else:
                for idx in range(len(truck_times)):
                    truck_times[idx] += 1

    # 다리 위에 트럭이 없는 조건
    else:
        trucks_on_bridge.append(weights[truck_idx])
        truck_weights_sum_on_bridge += weights[truck_idx]
        truck_times.append(1)
        truck_idx += 1
    
    total_time += 1

total_time += w
print(total_time)
