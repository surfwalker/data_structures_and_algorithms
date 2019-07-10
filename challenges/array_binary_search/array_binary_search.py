def array_binary_search(arr, val):
  
  half = (len(arr) + (len(arr) % 2)) // 2

  for i in range(0, half):
    if arr[i] == val:
      return i
  
  for i in range(half, len(arr)):
    if arr[i] == val:
      return i
  
  return -1