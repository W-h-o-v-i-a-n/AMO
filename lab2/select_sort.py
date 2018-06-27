def select_sort_min(arr: list):
    if len(arr) == 0:
        return
    for j in range(len(arr)):
        _min = j
        for i in range(j+1, len(arr)):
            if arr[i] < arr[_min]:
                _min = i
        if _min != j:
            value = arr[_min]
            for l in range(_min, j-1, -1):
                arr[l] = arr[l-1]
            arr[j] = value
    return arr


def select_sort_max(arr: list):
    if len(arr) == 0:
        return
    for j in range(len(arr)-1, -1, -1):
        _max = j
        for i in range(len(arr)-1, j-1, -1):
            if arr[i] > arr[_max]:
                _max = i
        if _max != j:
            value = arr[_max]
            for l in range(j+1, _max,):
                arr[l] = arr[l-1]
            arr[j] = value
    return arr


def count_sort_time(length: int, step: int=1):
    from random import randint
    from time import clock

    n_time = dict()
    for j in range(0, length+1, step):
        r = []
        for i in range(0, j):
            new = randint(-100000000001, 100000000001)
            if new not in r:
                r.append(new)
            else:
                i -= 1
        t1 = clock()
        select_sort_min(r)
        t2 = clock()
        n_time.update([(j, round(t2-t1, 10))])
    return n_time


# print(count_sort_time(100000, 100000))

