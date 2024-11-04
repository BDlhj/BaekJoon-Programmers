def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_names = {name: [] for name in id_list}
    report_receive_count = {name: 0 for name in id_list}
    
    for rep in report:
        from_, to_ = rep.split()
        if to_ not in report_names[from_]:
            report_names[from_].append(to_)
            report_receive_count[to_] += 1
    
    over_k = [element[0] for element in report_receive_count.items() if element[1] >= k]
    
    for i in range(len(id_list)):
        for name in report_names[id_list[i]]:
            if report_receive_count[name] >= k:
                answer[i] += 1

    return answer