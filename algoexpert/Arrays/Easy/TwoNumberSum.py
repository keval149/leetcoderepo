#Two Number Sum
def twoNumberSum(array, targetSum):
    # Write your code here.
	result = []
	if targetSum == None:
		return result
	if array == None or len(array) < 2:
		return result
	hmap = {}
	
	for i in array:
		diff = targetSum - i
		if diff in hmap:
			result.append(diff)
			result.append(i)
			return result
		else:
			hmap[i] = i
	return result

