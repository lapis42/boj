"""BOJ9252: Longest Common Subsequence (LCS) 2"""

a, b = input(), input()
na, nb = len(a), len(b)

f = [[0] * nb for _ in range(na)]
arr = [[''] * nb for _ in range(na)]
for i in range(na):
    for j in range(nb):
        if a[i] == b[j]:
            if i > 0 and j > 0:
                arr[i][j] = arr[i - 1][j - 1] + a[i]
            else:
                arr[i][j] += a[i]
        else:
            if i > 0:
                if j > 0:
                    if len(arr[i - 1][j]) > len(arr[i][j -1]):
                        arr[i][j] = arr[i - 1][j]
                    else:
                        arr[i][j] = arr[i][j - 1]
                else:
                    arr[i][j] = arr[i - 1][j]
            elif j > 0:
                arr[i][j] = arr[i][j - 1]

print(len(arr[-1][-1]))

if arr[-1][-1]:
    print(arr[-1][-1])
