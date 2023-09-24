import sys
input = sys.stdin.readline

n, k = map(int, input().split())
deleted = [False] * (n+1)
done = False
cnt = 0

for i in range(2, n+1):
    if not deleted[i]:
        deleted[i] = True
        cnt += 1
        if cnt == k:
            print(i)
            break

        for j in range(2, n//i + 1):
            if not deleted[i*j]:
                deleted[i*j] = True
                cnt += 1
                if cnt == k:
                    print(i*j)
                    done = True
                    break
        if done:
            break