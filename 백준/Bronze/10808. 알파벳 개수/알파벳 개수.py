import string 

s = input()
alphabet = list(string.ascii_lowercase)
al_cnt = {key:0 for key in alphabet}

for c in s:
    al_cnt[c] += 1

for i in al_cnt.values():
    print(i, end=' ')