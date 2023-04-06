''''
def max_profit(prices, k, fee, day=0, shares=0, py=0):
    print(py)
    if day == len(prices):
        return py

    # Não faz nada
    py1 = max_profit(prices, k, fee, day + 1, shares, py)

    # Compra uma ação
    py2 = py
    if shares < k and (day == 0 or prices[day] < prices[day - 1]):
        py2 = max_profit(prices, k, fee, day + 1, shares + 1, py - prices[day] - fee)

    # Vende uma ação
    py3 = py
    if shares > 0:
        py3 = max_profit(prices, k, fee, day + 1, shares - 1, py + prices[day])

    return max(py1, py2, py3)
'''


def max_profit(prices, k, fee, memo, day=0, shares=0, py=0):

    #if (day, shares) in memo:
        #print("ll")
    #    return memo[(day, shares)]
    if day == len(prices):
        #memo[(day, shares)] = py
        if (day,shares) in memo:
            print(memo[(day, shares)],py)
        #print(py)
        return py
    # Não faz nada
    py1 = max_profit(prices, k, fee, memo, day + 1, shares, py)

    # Compra ações
    py2 = float('-inf')
    for i in range(1, k - shares + 1):
        if day == 0 or prices[day] < prices[day - 1]:
            py2 = max(py2, max_profit(prices, k, fee, memo, day + 1, shares + i, py - prices[day] * i - fee * i))

    # Vende ações
    py3 = float('-inf')
    for i in range(1, shares + 1):
        py3 = max(py3, max_profit(prices, k, fee, memo, day + 1, shares - i, py + prices[day] * i))

    memo[(day, shares)] = max(py1, py2, py3)
    print(day,shares)
    return memo[(day, shares)]


if __name__ == "__main__":
    task = int(input())
    N, D, K, R = map(int, input().split())

    for i in range(N):
        shares = (list(map(int, input().split())))
        #print(len(shares))
        dp = {}
        profit = max_profit(shares, K, R,dp, 0, 0, 0)
        print(profit)

    memo = {}

    #print("best = ",best)
