first_case = list(map(int, input().split()))
second_case = list(map(int, input().split()))
third_case = list(map(int, input().split()))

answer = []
nums = [0, 1, 2, 3, 4]
names = ['E', 'A', 'B', 'C', 'D']

rule = dict(zip(nums, names))

answer.append(rule[first_case.count(0)])
answer.append(rule[second_case.count(0)])
answer.append(rule[third_case.count(0)])

for i in answer:
    print(i)