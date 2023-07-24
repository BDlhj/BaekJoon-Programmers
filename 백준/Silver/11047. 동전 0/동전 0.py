num_of_coins, target = list(map(int, input().split()))
count = 0
coins = []

for _ in range(num_of_coins):
    coins.append(int(input()))
coins.sort(reverse=True)

for coin in coins:
    count += (target // coin)
    target %= coin

print(count)