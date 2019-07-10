def insert_shift_array(lst, val):
  shifted_lst = [None] * (len(lst) + 1)
  half = (len(lst) + len(lst) % 2) // 2
  for item in range(len(lst) + 1):
    if item == half:
      shifted_lst[item] = val
    elif item < half:
      shifted_lst[item] = lst[item]
    else:
      shifted_lst[item] = lst[item -1]
  return(shifted_lst)
