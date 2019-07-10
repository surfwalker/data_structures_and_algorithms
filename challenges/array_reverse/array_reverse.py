def reverse_array1(arr):
    reversed_array = arr[::-1]
    print(reversed_array)

def reverse_array2(arr):
    half = len(arr) // 2
    right = -1
    for left in range(half):
        arr[left], arr[right] = arr[right], arr[left]
        right -= 1
    print(arr)

arr = [1, 2, 3, 4, 5]

reverse_array1(arr)
reverse_array2(arr)

