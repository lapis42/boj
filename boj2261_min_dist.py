import sys
r=sys.stdin.readline

dist = lambda x,y: (x[0]-y[0])**2 + (x[1]-y[1])**2

def bisect_right(p,x):
    lo=0
    hi=len(p)
    while lo < hi:
        mid = (lo+hi)//2
        if x < p[mid][0]: hi = mid
        else: lo = mid + 1
    return lo

def bisect_left(p,x):
    lo=0
    hi=len(p)
    while lo < hi:
        mid = (lo+hi)//2
        if p[mid][0] < x: lo = mid+1
        else: hi = mid
    return lo

def min_dist(p,a,b):
    n=b-a
    if n==2:
        return dist(p[a],p[a+1])
    elif n==3:
        return min(dist(p[a],p[a+1]),dist(p[a+1],p[a+2]),dist(p[a+2],p[a]))

    mid=(a+b)//2
    ans=min(min_dist(p,a,mid),min_dist(p,mid,b))
    if ans==0: return 0
    bound=int(ans**0.5)
    border=p[mid][0]

    left=bisect_left(p[a:b],border-bound)+a
    right=bisect_right(p[a:b],border+bound)+a
    np=right-left
    if np>=2:
        ptemp=sorted(p[left:right],key=lambda x:x[1])
        for i in range(np):
            for j in range(i+1,np):
                if ptemp[j][1]-ptemp[i][1]>bound:
                    break
                elif ptemp[i][0]<border and ptemp[j][0]<border:
                    continue
                elif ptemp[i][0]>border and ptemp[j][0]>border:
                    continue
                d=dist(ptemp[i],ptemp[j])
                if d<ans:
                    ans=d
    return ans


n=int(r())
d=[list(map(int,r().split())) for i in range(n)]
d.sort()
print(min_dist(d,0,len(d)))
