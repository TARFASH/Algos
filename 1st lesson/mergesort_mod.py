global count_inv
count_inv = 0

def MergeSort(arr):
    result = []
    global count_inv
    c = len(arr) // 2
    left = arr[:c]
    right = arr[c:]

    if len(left) > 1:
        left = MergeSort(left)
    if len(right) > 1:
        right = MergeSort(right)

    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count_inv += len(left) - i
            j += 1
    if i < len(left):
        result.extend(left[i:])
    elif j < len(right):
        result.extend(right[j:])
    return result

n = int(input())
arra = [int(i) for i in input().split()]
MergeSort(arra)
print(count_inv)