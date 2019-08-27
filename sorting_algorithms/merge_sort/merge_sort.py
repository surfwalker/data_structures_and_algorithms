def merge_sort(lst):
    if len(lst) == 0:
        return "This is an empty list."
    else:
        length = len(lst)  
        if length > 1:
            middle = length // 2
            left = lst[:middle]
            right = lst[middle:]
            merge_sort(left)
            merge_sort(right)
            merge(left, right, lst)
        return lst

def merge(left, right, lst):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k +=1
    if i == len(left):
        for element in right[j:]:
            lst[k] = right[j]
            j += 1
            k += 1
    else:
        for element in left[i:]:
            lst[k] = left[i]
            i += 1
            k += 1