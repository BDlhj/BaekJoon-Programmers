def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    for lost_num in lost[::-1]:
        if lost_num in reserve[::-1]:
            lost.remove(lost_num)
            reserve.remove(lost_num)
    
    for reserve_num in reserve:
        if reserve_num - 1 in lost:
            lost.remove(reserve_num - 1)
        elif reserve_num + 1 in lost:
            lost.remove(reserve_num + 1)

    return n - len(lost)