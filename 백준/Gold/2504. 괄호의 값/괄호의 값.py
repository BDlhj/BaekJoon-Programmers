import sys
input = sys.stdin.readline

arr = input().rstrip()
l_s_paren = '('
r_s_paren = ')'
l_m_paren = '['
r_m_paren = ']'
paren_v_dict = {l_s_paren: 2, l_m_paren: 3}
is_error = False
stack = []
cur_v = 1
answer = 0

for i in range(len(arr)):
    if arr[i] in [l_s_paren, l_m_paren]:
        stack.append(arr[i])
        cur_v *= paren_v_dict[arr[i]]
        
    elif arr[i] == r_s_paren:
        if not stack or stack[-1] != l_s_paren:
            is_error = True
            break
        if arr[i-1] == l_s_paren:
            answer += cur_v
        stack.pop()
        cur_v = int(cur_v/paren_v_dict[l_s_paren])
    elif arr[i] == r_m_paren:
        if not stack or stack[-1] != l_m_paren:
            is_error = True
            break
        if arr[i-1] == l_m_paren:
            answer += cur_v
        stack.pop()
        cur_v = int(cur_v/paren_v_dict[l_m_paren])
        
if is_error or stack:
    print(0)
else:
    print(answer)