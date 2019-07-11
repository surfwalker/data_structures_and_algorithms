def array_binary_search(arr, val):

    if len(arr) == 0:
        return -1

    left = 0
    middle = (len(arr) + (len(arr) % 2)) // 2
    right = len(arr) - 1

    while left != right:
        if val < arr[middle]:
            right = middle
            middle = right // 2
        if val > arr[middle]:
            left = middle
            middle = right - (right - left) // 2
        if val == arr[middle]:
            print(f"Index of target value is {middle}")
            return middle

    print(f"Target value of {val} was not found")
    return -1
