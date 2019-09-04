import statistics

def quick_sort(lst, left, right):
    if len(lst) == 0:
        return "This is an empty list."
    elif len(lst) == 1:
        return "List is already sorted."
    else:
        if left < right:
            partition_value = partition(lst, left, right)
            quick_sort(lst, left, partition_value - 1)
            quick_sort(lst, partition_value + 1, right)
	
def get_pivot(lst, left, right):
	middle = (right + left) // 2
	return statistics.median([left, middle, right])
	
def partition(lst, left, right):
	pivot_index = get_pivot(lst, left, right)
	pivot_value = lst[pivot_index]
	lst[pivot_index], lst[left] = lst[left], lst[pivot_index]
	border = left
	for index in range(left, right+1):
		if lst[index] < pivot_value:
			border += 1
			lst[index], lst[border] = lst[border], lst[index]
	lst[left], lst[border] = lst[border], lst[left]
	return border
