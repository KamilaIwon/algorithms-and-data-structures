import math


def bubble_sort_r(tab: []) -> []:
    n = len(tab)
    for k in range(n-1, 0, -1):
        for j in range(0, k):
            if tab[j] > tab[j+1]:
                tmp = tab[j]
                tab[j] = tab[j+1]
                tab[j+1] = tmp
    return tab


def binary_search(tab: [], value: int) -> bool:
    numbers = []
    # kopiujemy tablice
    for i in tab:
        numbers.append(i)

    # sortujemy tablice
    numbers = bubble_sort_r(numbers)

    start = 0
    kon = len(tab)-1
    while start <= kon:
        middle = math.floor((start + kon)/2)
        if numbers[middle] == value:
            return True
        elif numbers[middle] < value:
            start += 1
        else:
            kon -= 1
    return False


R = [0, 0, 0, 0, 0]
J = [2, 0, 7, 3, 4, 5, 8, 6, 9, 1]
print(binary_search(J, 0))
print(binary_search(R, 18))
