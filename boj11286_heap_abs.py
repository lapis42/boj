#used the standard library heapq
import sys
input = sys.stdin.readline

def push(heap,item):
    heap.append(item)
    pos=len(heap)-1
    while pos>0:
        parentpos=(pos-1)//2
        parent=heap[parentpos]
        if abs(item)<abs(parent) or (abs(item)==abs(parent) and item<parent):
            heap[pos]=parent
            pos=parentpos
        else:
            break
    heap[pos]=item

def pop(heap):
    item=heap.pop()
    if heap:
        returnitem=heap[0]

        pos=0
        child=1
        while child<len(heap):
            child2=child+1
            if child2<endpos and (abs(heap[child2])<abs(heap[child]) or (abs(heap[child2]==heap[child]) and child2<child)):
                child=child2
            heap[pos]=heap[child]
            pos=child
            child=2*pos+1
        heap[pos]=item

        while pos>0:
            parentpos=(pos-1)//2
            parent=heap[parentpos]
            if abs(item)<abs(parent) or (abs(item)==abs(parent) and item<parent):
                heap[pos]=parent
                pos=parentpos
            else:
                break
        heap[pos]=item

        return returnitem
    return item


heap=[]
n=int(input())
for i in range(n):
    x=int(input())
    if x:
        push(heap,x)
    elif heap:
        print(pop(heap))
    else:
        print(0)

