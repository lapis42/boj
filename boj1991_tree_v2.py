def transversal(mode, node='A'):
    l_node, r_node = tree[node]
    d = [node]
    l = transversal(mode, l_node) if l_node != '.' else []
    r = transversal(mode, r_node) if r_node != '.' else []
    if mode == 0:
        ans = d + l + r
    elif mode == 1:
        ans = l + d + r
    else:
        ans = l + r + d
    return ans


tree = {}
for i in range(int(input())):
    d, l, r = input().split()
    tree[d] = (l, r)

print(*transversal(0), sep='')
print(*transversal(1), sep='')
print(*transversal(2), sep='')
