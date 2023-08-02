a, b = input().split()
a = int(a)
b = int(b)

if a >= b:
    a, b = b, a

gap = b - a - 1 if a != b else 0
print(gap)

for num in range(a+1, b):
    print(num)