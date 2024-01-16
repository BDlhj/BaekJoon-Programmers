import sys
input = sys.stdin.readline

L = int(input())
string = input().rstrip()
char_num = {chr(key):value+1 for value, key in enumerate(range(97, 123))}
r = 31
mod = 1234567891

hash_value = 0
for i in range(L):
    hash_value += ((char_num[string[i]] * r ** i) % mod)

print(hash_value)