def bin_search_recursive(req, lst):
    left = 0
    right = len(lst) - 1

    while left <= right:
        middle = (left + right) // 2
        if lst[middle] == req:
            return middle
        elif lst[middle] > req:
            right = middle - 1
        else:
            left = middle + 1
    else:
        return 'Не найдено'


init_lst = list(i for i in range(15))
print(bin_search_recursive(15, init_lst))
