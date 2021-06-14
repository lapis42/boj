import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def solve(i, state):
    print(i, state)
    if i >= n * m:
        return 0
    if dp[i][state] == -1:
        if state & 1:
            dp[i][state] = solve(i + 1, state >> 1)
        else:
            # pass
            dp[i][state] = solve(i + 1, state >> 1)

            # vertical
            if i // m < n - 1:
                dp[i][state] = max(
                    dp[i][state],
                    solve(i + 1, (state >> 1) | (1 << m - 1)) +
                    price[grade[i] - 65][grade[i + m] - 65])

            # horizontal
            if i % m < m - 1 and not state >> 1 & 1:
                dp[i][state] = max(
                    dp[i][state],
                    solve(i + 2, state >> 2) +
                    price[grade[i] - 65][grade[i + 1] - 65])
    return dp[i][state]


price = [[10, 8, 7, 5, 0, 1], [8, 6, 4, 3, 0, 1], [7, 4, 3, 2, 0, 1],
         [5, 3, 2, 2, 0, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0]]

n, m = map(int, input().split())
grade = []
for _ in range(n):
    grade.extend(list(map(ord, input().rstrip())))

dp = [[-1] * (1 << m) for _ in range(n * m)]
print(solve(0, 0))
