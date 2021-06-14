import sys
input = sys.stdin.readline

max_distance = 10000000


def floyd_warshall(n_node, d):
    for m in range(n_node):
        for s in range(n_node):
            for e in range(n_node):
                if d[s][e] > d[s][m] + d[m][e]:
                    d[s][e] = d[s][m] + d[m][e]


def main():
    n_node = int(input())
    n_edge = int(input())

    d = [[max_distance] * n_node for _ in range(n_node)]
    for i in range(n_node):
        d[i][i] = 0
    for _ in range(n_edge):
        a, b, c = map(int, input().split())
        if d[a - 1][b - 1] > c:
            d[a - 1][b - 1] = c

    floyd_warshall(n_node, d)

    for i in d:
        for j in i:
            if j < max_distance:
                print(j, end=' ')
            else:
                print(0, end=' ')
        print()


if __name__ == '__main__':
    main()
