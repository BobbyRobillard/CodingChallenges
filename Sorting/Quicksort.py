def quick_sort(lst):
    if len(lst) < 2:
        return lst
    pivot = lst[0]
    lower = [i for i in lst[1:] if i <= pivot]
    higher = [i for i in lst[1:] if i > pivot]
    return quick_sort(lower) + [pivot] + quick_sort(higher)

print(quick_sort([4,1,5,2]))