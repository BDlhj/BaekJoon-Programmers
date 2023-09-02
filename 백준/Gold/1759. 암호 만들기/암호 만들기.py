import sys
input = sys.stdin.readline

l, c = map(int, input().split())
letters = input().split()
is_used = [False] * c
answer = [''] * (l+1)
vowel = ['a', 'e', 'i', 'o', 'u']
result = []

def backtrack(k):
    vowel_cnt = 0
    consonant_cnt = 0

    if k == l+1:
        for letter in answer[1:]:
            if letter in vowel:
                vowel_cnt += 1
            else:
                consonant_cnt += 1
        if vowel_cnt >= 1 and consonant_cnt >= 2:
            result.append(''.join(answer[1:]))
        return

    for i in range(c):
        if not is_used[i] and (letters[i] > answer[k-1]):
            is_used[i] = True
            answer[k] = letters[i]
            backtrack(k+1)
            is_used[i] = False

backtrack(1)

result.sort()
for i in result:
    print(i)