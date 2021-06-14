def kmp_table(p):
    pos = 1
    cnd = 0
    T = [-1] * (len(p) + 1)
    while pos < len(p):
        if p[pos] == p[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and p[pos] != p[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    T[pos] = cnd
    return T


def kmp_search(t, p):
    T = kmp_table(p)
    j = k = 0
    idx = []
    while j < len(t):
        if p[k] == t[j]:
            j += 1
            k += 1
            if k == len(p):
                idx.append(j - k + 1)
                k = T[k]
        else:
            k = T[k]
            if k < 0:
                j += 1
                k += 1
    return idx


t = input()
p = input()

idx = kmp_search(t, p)

print(len(idx))
print(*idx)
