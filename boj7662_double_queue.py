import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def flush(t):
    if t > 0:
        while q_max and d_max and d_max[0] == q_max[0]:
            heappop(q_max)
            heappop(d_max)
    else:
        while q_min and d_min and d_min[0] == q_min[0]:
            heappop(q_min)
            heappop(d_min)

for _ in range(int(input())):
    q_min, q_max = [], []
    d_min, d_max = [], []

    for _ in range(int(input())):
        c, v = input().split()
        x = int(v)

        if c == 'I':
            heappush(q_min, x)
            heappush(q_max, -x)
        elif c == 'D':
            flush(x)
            if x == 1:
                if q_max:
                    heappush(d_min, -heappop(q_max))
            else:
                if q_min:
                    heappush(d_max, -heappop(q_min))

    flush(1)
    flush(-1)
    if q_min and q_max:
        print(-q_max[0], q_min[0])
    else:
        print('EMPTY')
