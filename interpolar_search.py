

def bubble_sort_r(tab: []) -> []:
    n = len(tab)
    for k in range(n-1, 0, -1):
        for j in range(0, k):
            if tab[j] > tab[j+1]:
                tmp = tab[j]
                tab[j] = tab[j+1]
                tab[j+1] = tmp
    return tab


def interpolation_search(arr, n, x):

    lo = 0
    hi = (n - 1)

    while lo <= hi and arr[lo] <= x <= arr[hi]:
        if lo == hi:
            if arr[lo] == x:
                return lo
            return -1

        pos = lo + int(((float(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo])))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            lo = pos + 1

        else:
            hi = pos - 1

    return -1


arr = [1, 10, 20, 47, 50, 60, 70, 80, 90, 100]
x = 50
n = len(arr)
result = interpolation_search(arr, n, x)
print(result)
