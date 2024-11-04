def solution(video_len, pos, op_start, op_end, commands):
    video_len_min, video_len_sec = map(int, video_len.split(':'))
    pos_min, pos_sec = map(int, pos.split(':'))
    op_start_min, op_start_sec = map(int, op_start.split(':'))
    op_end_min, op_end_sec = map(int, op_end.split(':'))
    
    video_len_total_sec = video_len_min * 60 + video_len_sec
    pos_total_sec = pos_min * 60 + pos_sec
    op_start_total_sec = op_start_min * 60 + op_start_sec
    op_end_total_sec = op_end_min * 60 + op_end_sec

    for command in commands:
        if op_start_total_sec <= pos_total_sec <= op_end_total_sec:
            pos_total_sec = op_end_total_sec
    
        if command == 'prev':
            pos_total_sec = max(pos_total_sec - 10, 0)
        else:
            pos_total_sec = min(pos_total_sec + 10, video_len_total_sec)
    
    if op_start_total_sec <= pos_total_sec <= op_end_total_sec:
        pos_total_sec = op_end_total_sec
    

    res_min, res_sec = divmod(pos_total_sec, 60)
    
    return f'{res_min:02d}:{res_sec:02d}'