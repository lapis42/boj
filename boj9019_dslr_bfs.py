from collections import deque

for _ in range(int(input())):
    a, b = map(int, input().split())

    visited = [0] * 10000
    track = [0] * 10000
    method = [0] * 10000
    cmd_name = ['D', 'S', 'L', 'R']

    Q = deque([a])
    while Q:
        now = Q.popleft()

        if now == b:
            break

        cmds = [(2 * now) % 10000, (now - 1) if now > 0 else 9999,
                now % 1000 * 10 + now // 1000, now % 10 * 1000 + now // 10]
        for i, c in enumerate(cmds):
            if visited[c] == 0:
                visited[c] = 1
                track[c] = now
                method[c] = i
                Q.append(c)

    # backward
    i = b
    ans = ''
    while i != a:
        ans += cmd_name[method[i]]
        i = track[i]

    print(ans[::-1])
