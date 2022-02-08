#isValidSubsequence

def isValidSubsequence(array, sequence):
    # Write your code here.
	
	if array == None or len(array) <= 0:
		return False
	if sequence == None or len(array) <= 0:
		return False
	if len(sequence) > len(array):
		return False
	
	i = 0
	j = 0

	while(i < len(array) and j < len(sequence)):
		if(array[i] == sequence[j]):
			i = i + 1
			j = j + 1
		else:
			i = i + 1

	if(j == len(sequence)):
		return True
	else:
		return False
