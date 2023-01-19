import math

def bubble_sort_r(tab: []) -> []:
    n = len(tab)
    for k in range(n-1, 0, -1):
        for l in range (0, k):
            if tab[l] > tab[l+1]:
                tmp = tab[l]
                tab[l] = tab[l+1]
                tab[l+1] = tmp
    return tab


def binarysearch(tab: [], value: int) -> bool:
    numbers = []
    for i in tab:
        numbers.append(i)

    numbers = bubble_sort_r(numbers)

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

J = [2, 0, 7, 3, 4, 5, 8, 6, 9, 1]
print(binarysearch(J, 3))
print(J)