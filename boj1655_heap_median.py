import sys
from heapq import heappush,heappop
input=sys.stdin.readline
minheap=[]
maxheap=[]
for i in range(int(input())):
    x=int(input())

    if not maxheap:
        heappush(maxheap,-x)
    elif len(maxheap)>len(minheap):
        if x>-maxheap[0]:
            heappush(minheap,x)
        else:
            heappush(maxheap,-x)
            heappush(minheap,-heappop(maxheap))
    else:
        if x<minheap[0]:
            heappush(maxheap,-x)
        else:
            heappush(minheap,x)
            heappush(maxheap,-heappop(minheap))
    print(-maxheap[0])


