def hasSingleCycle(array):
	visited = 0
	cur = 0
	while visited < len(array):
		if visited > 0 and cur == 0:
			return False
		visited+=1
		cur = helper(cur,array)
	return cur == 0

def helper(idx, array):
	jump = array[idx]
	nextidx = (jump + idx) % len(array)
	
	if nextidx >=0:
		return nextidx
	else:
		return nextidx+len(array)
