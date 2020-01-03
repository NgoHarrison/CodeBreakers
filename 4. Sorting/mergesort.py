def mergeSort(arrayay):
    _mergesort(arrayay,0,len(arrayay)-1)
	return arrayay
    
def _mergesort(arrayay,lo,hi):
	if lo >=hi:
		return
	
	mid = ((lo+hi)//2)+1
	
	_mergesort(arrayay,lo,mid-1)
	_mergesort(arrayay,mid,hi)
	
	merge(arrayay,lo,mid,hi)
	
def merge(array,lo,mid,hi):
	copy = array[:]
	cur = lo
	curs1=lo
	curs2=mid
	
	while cur<=hi:
		if curs1 < mid and curs2 <=hi:
			if copy[curs1] < copy[curs2]:
				array[cur] = copy[curs1]
				curs1+=1
			else:
				array[cur]=copy[curs2]
				curs2+=1
		elif curs1 < mid:
			array[cur]=copy[curs1]
			curs1+=1
		else:
			array[cur] = copy[curs2]
			curs2+=1
		cur+=1
