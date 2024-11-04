from collections import deque


def solution(cards1, cards2, goal):
    cards1_queue = deque(cards1)
    cards2_queue = deque(cards2)
    completed_sentence = []
    
    for goal_word in goal:
        if cards1_queue and cards1_queue[0] == goal_word:
            completed_sentence.append(cards1_queue.popleft())
        elif cards2_queue and cards2_queue[0] == goal_word:
            completed_sentence.append(cards2_queue.popleft())
        
    if completed_sentence == goal:
        return 'Yes'
    return 'No'