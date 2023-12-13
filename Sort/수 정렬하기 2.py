#BAEKJOON 2751
#합병정렬
import sys

def Merge_sort(A):
    if len(A) < 2:
        return A

    mid = len(A) // 2
    left_arr = Merge_sort(A[:mid])
    right_arr = Merge_sort(A[mid:])
    return Merge(left_arr, right_arr)

def Merge(left, right):
    merged = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else :
            merged.append(right[r])
            r += 1

    while l < len(left):
        merged.append(left[l])
        l += 1
    while r < len(right):
        merged.append(right[r])
        r += 1
    return merged

n = int(sys.stdin.readline())
Arr = []
for i in range(n):
    Arr.append(int(sys.stdin.readline()))
Arr = Merge_sort(Arr)
for i in range(n):
    print(Arr[i])