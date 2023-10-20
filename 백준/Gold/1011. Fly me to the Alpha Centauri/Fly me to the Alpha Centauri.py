T = int(input())
for i in range(T):
  x, y = map(int, input().split())
  d = y - x
  cnt = 0
  sum = 1
  add = 1
  while d > sum:
    if cnt == 0:
      sum += add
      cnt += 1
    else:
      add += 1
      sum += add
      cnt = 0
  if cnt == 0:
    print(add * 2 - 1)
  else:
    print(add * 2)