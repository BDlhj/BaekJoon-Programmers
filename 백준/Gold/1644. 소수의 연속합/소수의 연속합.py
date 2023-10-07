import sys
import math
input = sys.stdin.readline

n = int(input())
array = [True for i in range(n + 1)]

if n == 1:
    print(0)

else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2 
            while i * j <= n:
                array[i * j] = False
                j += 1

    prime_nums = [i for i in range(2, n+1) if array[i]]
    st = en = 0
    answer = 0
    partial_sum = prime_nums[en]

    while True:
        if partial_sum < n:
            en += 1
            if en == len(prime_nums):
                break
            partial_sum += prime_nums[en]
        elif partial_sum > n:
            partial_sum -= prime_nums[st]
            st += 1
        else:
            answer += 1
            partial_sum -= prime_nums[st]
            st += 1

    print(answer)