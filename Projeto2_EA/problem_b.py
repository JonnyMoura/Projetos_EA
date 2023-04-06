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


def max_profit(prices, k, fee):
    n = len(prices)
    dp = [[0 for _ in range(k + 1)] for _ in range(n)]

    for j in range(k + 1):
        dp[0][j] = -prices[0] * j - fee * j

    for i in range(1, n):
        for j in range(k + 1):
            # Não faz nada
            #py1 = dp[i - 1][j]

            # Compra ações
            py2 = dp[i - 1][j]
            for m in range(1, j + 1):
                py2 = max(py2, dp[i - 1][j - m] - prices[i] * m - fee * m)

            # Vende ações
            py3 = dp[i - 1][j]
            for m in range(1, k - j + 1):
                py3 = max(py3, dp[i - 1][j + m] + prices[i] * m)

            dp[i][j] = max( py2, py3)
    #print(dp)
    return dp[n - 1][0]


if __name__ == "__main__":
    task = int(input())
    N, D, K, R = map(int, input().split())

    for i in range(N):
        shares = (list(map(int, input().split())))
        #print(len(shares))
        dp = {}
        profit = max_profit(shares, K, R)
        print(profit)

    #memo = {}

    #print("best = ",best)
