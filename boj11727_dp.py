n = int(input())
dp = [1, 1, 3]
for i in range(3, n + 1):
    j = i % 3
    dp[j] = (dp[j - 1] + 2 * dp[j - 2]) % 10007
print(dp[n % 3])
