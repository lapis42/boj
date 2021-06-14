def ispalindrome(i, j):
    if cache[i][j] == -1:
        if s[i] == s[j] and (j - i < 2 or ispalindrome(i + 1, j - 1)):
            cache[i][j] = 1
        else:
            cache[i][j] = 0
    return cache[i][j]


s = __import__('sys').stdin.readline().rstrip()
n = len(s)

cache = [[-1] * (n + 1) for _ in range(n + 1)]
dp = [0] * (n + 1)
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    for j in range(1, i):
        if ispalindrome(j - 1, i - 1):
            dp[i] = min(dp[i], dp[j - 1] + 1)

print(dp[-1])
