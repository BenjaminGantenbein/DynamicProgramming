def KnapSack(values, weights, sum):

    n = len(weights)

    dp=[[0 for x in range(sum+1)] for y in range(n+1)]

    for i in range(n+1):
        for j in range(sum+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif j >= weights[i-1]:
                dp[i][j] = max(dp[i-1][j], values[i-1] + dp[i-1][j-weights[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][sum]


values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

result = KnapSack(values, weights, capacity)
print(result)
