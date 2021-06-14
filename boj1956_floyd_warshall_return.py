import sys
input = sys.stdin.readline

dist_max = sys.maxsize


def floyd_warshall(d, n_node):
    for m in range(n_node):
        for s in range(n_node):
            for e in range(n_node):
                if d[s][e] > d[s][m] + d[m][e]:
                    d[s][e] = d[s][m] + d[m][e]


def main():
    n_node, n_edge = map(int, input().split())

    d = [[dist_max] * n_node for _ in range(n_node)]
    for _ in range(n_edge):
        a, b, c = map(int, input().split())
        if c < d[a - 1][b - 1]:
            d[a - 1][b - 1] = c

    floyd_warshall(d, n_node)

    min_d = dist_max
    for i in range(n_node):
        if d[i][i] < min_d:
            min_d = d[i][i]

    if min_d == dist_max:
        print(-1)
    else:
        print(min_d)


if __name__ == "__main__":
    main()
