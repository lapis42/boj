# BOJ1644


def prime(n):
    arr = [0] * 2 + [1] * (n - 1)
    for i in range(2, int(n**0.5) + 1):
        if arr[i]:
            for j in range(2 * i, n + 1, i):
                arr[j] = 0
    return [i for i in range(2, n + 1) if arr[i]]


def main():
    n = int(input())
    if n==1:
        print(0)
        return

    arr = prime(n)
    n_prime = len(arr)
    j = 0
    s = arr[0]
    cnt = 0

    for i in range(n_prime):
        while s < n and j < n_prime - 1:
            j += 1
            s += arr[j]

        if s < n:
            break
        elif s == n:
            cnt += 1
        s -= arr[i]

    print(cnt)


if __name__ == "__main__":
    main()
