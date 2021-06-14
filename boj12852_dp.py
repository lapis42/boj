n = int(input())

cnt = [n] * (n + 1)
cnt[1] = 0
path = [[] for _ in range(n + 1)]
path[1] = [1]

for i in range(2, n + 1):
    temp = [cnt[i - 1]]
    ptemp = [path[i - 1]]
    if i % 3 == 0:
        temp.append(cnt[i // 3])
        ptemp.append(path[i // 3])
    if i % 2 == 0:
        temp.append(cnt[i // 2])
        ptemp.append(path[i // 2])

    min_temp = min(temp)
    cnt[i] = min_temp + 1
    path[i] = [i] + ptemp[temp.index(min_temp)]

print(cnt[-1])
print(*path[-1])
