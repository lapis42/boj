from collections import deque

n, k = map(int, input().split())

cnt = [0] * 100001
track = [0] * 100001

q = deque([n])
while q:
    now = q.popleft()
    if now == k:
        break
    after = [now - 1, now + 1, 2 * now]
    for i in after:
        if 0 <= i <= 100000 and cnt[i] == 0:
            cnt[i] = cnt[now] + 1
            track[i] = now
            q.append(i)

# backtracking
ans = [k]
i = k
while i != n:
    i = track[i]
    ans.append(i)

print(cnt[k])
print(*ans[::-1])
