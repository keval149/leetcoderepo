#Sorted Squared Array

def sortedSquaredArray(array):
    # Write your code here.
	left = 0
	right = len(array)-1
	n = len(array)
	result = [0] * n
	ptr = len(result)-1
	while(left <= right):
		if (abs(array[left]) < abs(array[right])):
			result[ptr]= array[right]*array[right]
			right = right - 1
		else:
			result[ptr]= array[left]*array[left]
			left = left + 1
		ptr = ptr - 1

    return result
