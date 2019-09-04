def insert_sort(lst):
    if len(lst) == 0:
        return "This is an empty list."
    else:
        for index in range(1, len(lst)):
            marker = index - 1
            while lst[marker] > lst[marker + 1] and marker >= 0:
                lst[marker], lst[marker + 1] = lst[marker + 1], lst[marker]
                marker -= 1
        return lst
