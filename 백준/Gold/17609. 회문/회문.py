import sys
input = sys.stdin.readline

def check_palindrome(string):
    if string == string[::-1]:
        return 0
    
    s_idx = 0
    e_idx = len(string) - 1

    while string[s_idx] == string[e_idx]:
        s_idx += 1
        e_idx -= 1
    
    sub_string = string[s_idx:e_idx+1]
    sub_string_popped_left = sub_string[1:]
    sub_string_popped_right = sub_string[:-1]
    if sub_string_popped_left == sub_string_popped_left[::-1]:
        return 1
    elif sub_string_popped_right == sub_string_popped_right[::-1]:
        return 1

    return 2

t = int(input())
for _ in range(t):
    print(check_palindrome(input().rstrip()))