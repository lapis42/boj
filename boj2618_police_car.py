"""BOJ2618: Shortest path"""
import sys
input = sys.stdin.readline


def d(i, j):
    if i > 0 and j > 0:
        return abs(case[i - 1][0] - case[j - 1][0]) + abs(case[i - 1][1] -
                                                          case[j - 1][1])
    elif j == 0:  # a is moving
        return abs(case[i - 1][0] - 1) + abs(case[i - 1][1] - 1)
    else:  # b is moving
        return abs(case[j - 1][0] - n) + abs(case[j - 1][1] - n)


def my_min(f, i, axis):
    idx = 0
    if axis == 0:  # column
        m = f[0][i] + d(i + 1, 0)
        for j in range(1, i):
            if m > f[j][i] + d(i + 1, j):
                m = f[j][i] + d(i + 1, j)
                idx = j
    else:
        m = f[i][0] + d(0, i + 1)
        for j in range(1, i):
            if m > f[i][j] + d(j, i + 1):
                m = f[i][j] + d(j, i + 1)
                idx = j
    return m, idx


n = int(input())
w = int(input())
case = [list(map(int, input().split())) for _ in range(w)]

f = [[sys.maxsize] * (w + 1) for _ in range(w + 1)]
f[0][0] = 0
f[1][0] = d(1, 0)
f[0][1] = d(0, 1)
fwhere = [[0] * (w + 1) for _ in range(w + 1)]

# forward
for i in range(w + 1):
    for j in range(w + 1):
        if (i < 2 and j < 2) or i == j:
            continue
        if j > i:
            if j == i + 1:
                f[i][j], fwhere[i][j] = my_min(f, i, 1)
            else:
                f[i][j] = f[i][j - 1] + d(j - 1, j)
                fwhere[i][j] = j - 1
        else:
            if i == j + 1:
                f[i][j], fwhere[i][j] = my_min(f, j, 0)
            else:
                f[i][j] = f[i - 1][j] + d(i, i - 1)
                fwhere[i][j] = i - 1

# backward
m_a = min(f[-1])
idx_a = f[-1].index(m_a)

m_b = f[0][-1]
idx_b = 0
for i in range(1, w + 1):
    if m_b > f[i][-1]:
        m_b = f[i][-1]
        idx_b = i

choice = [0] * (w + 1)
if m_a < m_b:
    choice[-1] = 1
    a = w
    b = idx_a
    ans = m_a
else:
    choice[-1] = 2
    a = idx_b
    b = w
    ans = m_b

i = w
while i > 0:
    if a > b:
        a = fwhere[a][b]
        choice[i] = 1
    else:
        b = fwhere[a][b]
        choice[i] = 2
    i -= 1

print(ans)
print(*choice[1:], sep='\n')
