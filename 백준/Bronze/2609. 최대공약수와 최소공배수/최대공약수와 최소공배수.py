import sys
input = sys.stdin.readline

num1, num2 = map(int, input().split())
gcd, lcm = 0, 0

for i in range(1, min(num1, num2)+1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

lcm = gcd * (num1 // gcd) * (num2 // gcd)

print(gcd)
print(lcm)
