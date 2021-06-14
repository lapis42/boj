import sys
from bisect import bisect
sys.setrecursionlimit(100000)
input = sys.stdin.readlines



def postorder(s, e):
    if s == e: return
    d = preorder[s]
    idx = bisect(preorder, d, s, e)
    postorder(s + 1, idx)
    postorder(idx, e)
    print(d)


preorder = list(map(int, input()))
postorder(0, len(preorder))
