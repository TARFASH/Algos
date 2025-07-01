# quicksort
import random


def QuickSort(array):
    if array == []:
        return array
    pivot = random.choice(array)
    lower = []
    equal = []
    greater = []
    for i in array:
        if i < pivot:
            lower.append(i)
        elif i > pivot:
            greater.append(i)
        else:
            equal.append(i)

    if len(lower) != 0:
        lower = QuickSort(lower)
    if len(greater) != 0:
        greater = QuickSort(greater)
    return lower + equal + greater


quant = int(input())
arr = [int(i) for i in input().split()]
print(*QuickSort(arr))
