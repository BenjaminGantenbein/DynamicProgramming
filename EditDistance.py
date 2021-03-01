def EditDistance_memoized(s1, s2, n, m, dp):

    if(n == 0):
        return m
    if(m == 0):
        return n

    if(dp[n][m] != -1):
        return dp[n][m]

    if(s1[n - 1] == s2[m - 1]):
        if(dp[n - 1][m - 1] == -1):
            dp[n][m] = EditDistance_memoized(s1, s2, n - 1, m - 1, dp)
            return dp[n][m]
        else :
            dp[n][m] = dp[n - 1][m - 1]
            return dp[n][m]
    else:
        if(dp[n-1][m] != -1):
            m1 = dp[n -1][m]
        else :
            m1 = EditDistance_memoized(s1, s2, n - 1, m, dp)
        if(dp[n][m-1] != -1):
            m2 = dp[n][m-1]
        else :
            m2 = EditDistance_memoized(s1, s2, n, m - 1, dp)
        if(dp[n - 1][m - 1] != -1):
            m3 = dp[n-1][m-1]
        else :
            m3 = EditDistance_memoized(s1, s2, n - 1, m - 1, dp)

        dp[n][m] = 1 + min(m1, min(m2, m3))
        return dp[n][m]

str1 = "kaesekuchen"
str2 = "kaeserfondue"

n = len(str1)
m = len(str2)
dp =[[-1 for i in range(m + 1)] for j in range(n + 1)]

print(EditDistance_memoized(str1, str2, n, m, dp))
