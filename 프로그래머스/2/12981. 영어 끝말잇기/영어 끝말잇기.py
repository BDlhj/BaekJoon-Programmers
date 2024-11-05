def solution(n, words):
    word_history = []
    for i in range(len(words)):
        if (words[i] in word_history) or (word_history and word_history[-1][-1] != words[i][0]):
            return [i % n + 1, i // n + 1]
        word_history.append(words[i])
    return [0, 0]