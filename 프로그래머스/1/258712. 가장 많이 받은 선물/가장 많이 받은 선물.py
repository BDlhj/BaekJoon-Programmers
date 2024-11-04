def solution(friends, gifts):
    friends_dict = {friend: i for i, friend in enumerate(friends)}
    gift_graph = [[0] * len(friends) for _ in range(len(friends))]
    
    for gift in gifts:
        giver, receiver = gift.split()
        gift_graph[friends_dict[giver]][friends_dict[receiver]] += 1

    rotated_gift_graph = list(zip(*gift_graph))
    gift_index_dict = {friend: (sum(gift_graph[i]) - sum(rotated_gift_graph[i])) for i, friend in enumerate(friends)}

    answer = [0] * len(friends)
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i == j:
                continue
            else:
                if gift_graph[i][j] > gift_graph[j][i]:
                    answer[i] += 1
                elif (gift_graph[i][j] == gift_graph[j][i]) and (gift_index_dict[friends[i]] > gift_index_dict[friends[j]]):
                    answer[i] += 1
    
    return max(answer)