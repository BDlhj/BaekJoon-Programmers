import sys
input = sys.stdin.readline

n, k = map(int, input().split())
devices = list(map(int, input().split()))
# multitab[i] : i 전기용품이 멀티탭에 꽂혀있다.
multitab = [0] * 101
answer = 0

for i in range(k):
    action = False

    # 멀티탭 안 찼으면 채우기
    if sum(multitab) < n:
        # print('멀티탭 채우기')
        multitab[devices[i]] = 1

    # 가득 찼으면 뺄 거 정하기
    else:
        # 이미 꽂혀있으면 다음 전기용품으로 넘어가기
        if multitab[devices[i]]:
            continue
        
        # 안 꽂혀있는거면 뺄 거 정하기
        li = []
        for j in range(i+1, k):
            # li가 n-1개면 그만
            if len(li) == n-1:
                break

            # 멀티탭에 있으면 안 뺄 목록에 넣기
            if multitab[devices[j]] and devices[j] not in li:
                li.append(devices[j])    

        # n-1개면 무조건 li에 없는 거 빼기
        for x in range(len(multitab)):
            if multitab[x] and x not in li:
                multitab[x] = 0
                multitab[devices[i]] = 1
                answer += 1
                action = True
                break
        if action:
            continue
            
print(answer)