def findThreeLargestNumbers(array):
  lst = [float("-inf"),float("-inf"),float("-inf")]
	for i in array:
		for j in range(-1,-4,-1):
			if lst[j] < i:
				for k in range(j+3):
					lst[k] = lst[k+1]
				lst[j] = i
				break
			
	return lst
