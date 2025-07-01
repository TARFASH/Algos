def get_max(array):
    result = 0
    for i in array:
        if i > result:
            result = i
    return result

def sort_n(num, array):
    result = []
    count = [0 for i in range(get_max(array)+1)]
    for i in array:
        count[i] += 1
    for i in range(len(count)):
        if count[i] != 0:
            for _ in range(count[i]):
                result.append(i)
    return result


n = int(input())
arr = [int(i) for i in input().split()]
print(*sort_n(n, arr))