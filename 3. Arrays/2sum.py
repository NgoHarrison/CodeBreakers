def twoNumberSum(array, target):
    comp = set()
    comp.add(array[0])
    for i in range(1,len(array)):
        if (target - array[i]) in comp:
	    return [array[i],target-array[i]]
	comp.add(array[i])
    return []
