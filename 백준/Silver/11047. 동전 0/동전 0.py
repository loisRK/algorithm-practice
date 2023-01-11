cnt, price = map(int, input().split())
coin_list = [int(input()) for _ in range(cnt)]
count = 0

coin_list.sort(reverse=True)

for coin in coin_list:
    count += (price // coin)
    price %= coin
    if(price == 0):
        break

print(count)