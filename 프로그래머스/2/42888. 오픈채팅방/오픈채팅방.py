def solution(record):
    uid_nickname = {}
    temp_result = []
    
    for rec in record:
        chunks = rec.split()
        if chunks[0] == 'Enter':
            uid_nickname[chunks[1]] = chunks[2]
            temp_result.append(('들어왔습니다.', chunks[1]))
        elif chunks[0] == 'Leave':
            temp_result.append(('나갔습니다.', chunks[1]))
        elif chunks[0] == 'Change':
            uid_nickname[chunks[1]] = chunks[2]
    
    result = [f'{uid_nickname[res[1]]}님이 {res[0]}' for res in temp_result]
    return result