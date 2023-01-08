import math
from typing import List
A = [6, 1, 7, 3, 4, 9, 2, 5, 8, 0]
B = [8, 5, 4, 2, 1, 7, 9, 6, 0, 3]
C = [3, 4, 0, 7, 1, 5, 2, 8, 9, 6]
D = [3, 4, 1, 2, 5, 0, 9, 8, 6, 7]
E = [3, 5, 8, 7, 1, 6, 9, 4, 0, 2]
F = [0, 7, 9, 4, 8, 6, 5, 3, 2, 1]
G = [9, 2, 1, 5, 8, 0, 6, 4, 3, 7]
H = [4, 5, 2, 7, 0, 9, 1, 3, 6, 8]
I = [0, 8, 2, 7, 6, 3, 9, 1, 5, 4]
J = [2, 0, 7, 3, 4, 5, 8, 6, 9, 1]


def bubble_sort_r(tab: []) -> []:
    n = len(tab)
    for k in range(n-1, 0, -1):
        for l in range (0, k):
            if tab[l] > tab[l+1]:
                tmp = tab[l]
                tab[l] = tab[l+1]
                tab[l+1] = tmp
    return tab


def bubble_sort_m(tab: []) -> []:
    n = len(tab)
    for k in range(n-2, 0, -1):
        for l in range(n-1, 0, -1):
            if tab[l] > tab[l-1]:
                tmp = tab[l]
                tab[l] = tab[l-1]
                tab[l-1] = tmp
    return tab


print(bubble_sort_r(A))
print(bubble_sort_m(B))


def selectionSort_r(tab: []) -> []:

    n = len(tab)
    for k in range(0, n):
        imin = k
        for l in range(k+1, n):
            if tab[imin] > tab[l]:
                imin = l
        if imin != k:
            tmp = tab[imin]
            tab[imin] = tab[k]
            tab[k] = tmp
    return tab

print(selectionSort_r(C))
print(selectionSort_r(D))


def insertion_sort_r(tab: []) -> []:
    n = len(tab)
    for k in range(1, n):
        key = tab[k]
        m = k
        for x in range(0, k):
            if tab[x] > key:
                m = x
                break
        if m == k:
            continue
        for j in range(k, m, -1):
            tab[j] = tab[j-1]
        tab[m] = key
    return tab


print(insertion_sort_r(F))


# binary seearch

def binarysearch(tab: [], value: int) -> bool:
    numbers = bubble_sort_r(tab)
    pocz = 0
    kon = len(tab)-1
    while pocz <= kon:
        middle = math.floor((pocz + kon)/2)
        if numbers[middle] == value:
            return True
        elif numbers[middle] < value:
            pocz += 1
        else:
            kon -= 1
    return False

