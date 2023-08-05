word1 = list(input())
word2 = list(input())

for i in word1[::-1]:
    if i in word2:
        word1.remove(i)
        word2.remove(i)

print(len(word1)+len(word2))