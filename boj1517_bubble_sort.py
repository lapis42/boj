import sys
input = sys.stdin.readline


def merge_sort(start, end):
    global ans
    if start == end:
        return

    mid = (start + end) // 2
    merge_sort(start, mid)
    merge_sort(mid + 1, end)

    temp = []
    i, j = start, mid + 1
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
            ans += mid + 1 - i
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= end:
        temp.append(arr[j])
        j += 1
    arr[start:end + 1] = temp


n = int(input())
arr = list(map(int, input().split()))
ans = 0
merge_sort(0, n - 1)
print(ans)
