def min_money_leftover(prices, money):
    money =3

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            total_price = prices[i] + prices[j]
            if total_price <= money:
                leftover = money - total_price
                min_leftover = min(min_leftover, leftover)

    return min_leftover

# Example usage:
prices = [3,2,3]
initial_money = 3
result = min_money_leftover(prices, initial_money)
print(result)
