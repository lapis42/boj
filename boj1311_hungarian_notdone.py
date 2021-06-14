# Hungarian method
import sys
r=sys.stdin.readline

# read data
n=int(r())
cost=[list(map(int,r().split())) for i in range(n)]

def solve(c):
    from functools import reduce
    from operator import mul

    # function for matrix manipulation
    transpose = lambda x: list(map(list, zip(*x)))
    normalize_row = lambda x: [[j-min(i) for j in i] for i in x]
    normalize_col = lambda x: transpose(normalize_row(transpose(x)))
    mark_zero = lambda x: [[1 if j==0 else 0 for j in i] for i in x]
    choice_row = lambda c: [i for i,v in enumerate(c) if sum(v)==0]
    choice_col = lambda c: choice_col

    n = len(cost)
    c = [[0]*n for i in range(n)] # choices

    # reduced to 0's by subtraction
    x = normalize_row(cost)
    x = normalize_col(x)

    k = 0
    while k < n:
        # choose a maximal indepedent set of k zeros and a minimal cover of k lines
        z = mark_zero(x)
        k = cover(z)

    # choose a maximal indepedent set of k zeros and a minimal cover of k lines
    def cover(z,c):
        row=set()
        col=set()
        # mark all rows in which no choice has been made
        row.add(choice_row(c))
        if not row:
            return n

        while True:
            # mark all columns not already marked which have zeros in marked rows
            c = mark_col(z)





