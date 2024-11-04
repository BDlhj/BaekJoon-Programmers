def solution(enroll, referral, seller, amount):
    result = {name: 0 for name in enroll}
    referral_graph = {name: ref for name, ref in zip(enroll, referral)}
    
    for i in range(len(seller)):
        child = seller[i]
        income = amount[i] * 100
        
        while referral_graph[child] != '-':
            contrib = income // 10 if income // 10 >= 1 else 0
            mine = income - contrib
            result[child] += mine
            
            if contrib == 0:
                break
            
            child = referral_graph[child]
            income = contrib
        else:
            contrib = income // 10 if income // 10 >= 1 else 0
            mine = income - contrib
            result[child] += mine
        
    return list(result.values())