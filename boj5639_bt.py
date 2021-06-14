import sys
input = sys.stdin.readlines


def push(arr, x):
    idx = 0
    while idx in arr:
        if x < arr[idx]:
            idx = 2 * idx + 1
        else:
            idx = 2 * idx + 2
    arr[idx] = x


def postorder(arr, idx):
    if idx in arr:
        postorder(arr, 2 * idx + 1)
        postorder(arr, 2 * idx + 2)
        print(arr[idx])


preorder = list(map(int, input()))

arr = {}
for x in preorder:
    push(arr, x)

postorder(arr, 0)
