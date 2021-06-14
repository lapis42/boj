"""BOJ145
O(n * 2**(n/2))
"""
from bisect import bisect


def calc_combination(x):
    n = len(x)
    arr = [0] * (2**n)

    for i in range(1, 2**n):
        for j in range(n):
            if i >> j & 1:
                arr[i] += x[j]

    return arr


def main():
    n, c = map(int, input().split())
    x = list(map(int, input().split()))

    # 2 * 2**(n/2) * (n/2) = n * 2**(n/2)
    arr_left = calc_combination(x[:n // 2])
    arr_right = calc_combination(x[n // 2:])
    arr_right.sort()

    # 2**(n/2) * log2(2**(n/2)) = n/2 * 2**(n/2)
    cnt = 0
    for i in arr_left:
        if c - i >= 0:
            cnt += bisect(arr_right, c - i)

    print(cnt)


if __name__ == "__main__":
    main()
