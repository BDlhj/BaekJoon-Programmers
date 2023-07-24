def solution(survey, choices):
    answer = ''
    scores = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for i in range(len(survey)):
        type_idx = choices[i] // 4
        score = abs(choices[i]-4)
        scores[survey[i][type_idx]] += score
        
    scores_list = list(scores.items())
    for j in range(len(scores_list)//2):
        if scores_list[2*j][1] < scores_list[2*j+1][1]:
            answer += scores_list[2*j+1][0]
        else:
            answer += scores_list[2*j][0]        
    
    return answer