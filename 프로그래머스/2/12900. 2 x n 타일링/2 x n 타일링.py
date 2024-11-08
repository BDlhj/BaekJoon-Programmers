def solution(n):
    memo = [0, 1, 2]
    if n == 1 or n == 2:
        return memo[n]
    else:
        for i in range(3, n + 1):
            memo.append((memo[i - 1] + memo[i - 2]) % 1000000007)
    
    return memo[-1]