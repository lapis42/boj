import sys
input = sys.stdin.readline

max_distance = 500 * 10000


def bellman_ford(edges, n_node):
    distance = [max_distance] * (n_node + 1)
    distance[1] = 0

    for _ in range(n_node):
        for a, b, c in edges:
            if distance[a] < max_distance and distance[a] + c < distance[b]:
                distance[b] = distance[a] + c

    for a, b, c in edges:
        if distance[a] < max_distance and distance[b] > distance[a] + c:
            return []
    return distance[2:]


def main():
    n_node, n_edge = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(n_edge)]

    dist = bellman_ford(edges, n_node)

    if dist:
        for i in dist:
            if i < max_distance:
                print(i)
            else:
                print(-1)
    else:
        print(-1)


if __name__ == "__main__":
    main()
