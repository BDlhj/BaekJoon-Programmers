def solution(N, stages):
    fail_ratio = {}
    player_num = len(stages)
    stage_fail_player_num = {stage: 0 for stage in range(1, N + 2)}
    
    stages.sort()
    for stage in stages:
        stage_fail_player_num[stage] += 1
    
    for stage in range(1, N + 1):
        if player_num == 0:
            fail_ratio[stage] = 0
            continue
        fail_ratio[stage] = stage_fail_player_num[stage] / player_num
        player_num -= stage_fail_player_num[stage]

    answer = sorted(fail_ratio, key = lambda x: fail_ratio[x], reverse=True)
    return answer