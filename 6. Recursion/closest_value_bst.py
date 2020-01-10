def findClosestValueInBst(tree, target):
    return helper(tree,target,float("inf"))

def helper(tree,target,curr):
    if tree is None:
	return curr
    if abs(target - tree.value) < abs(target - curr):
	curr = tree.value
	
    if target < tree.value:
	return helper(tree.left,target,curr)
    elif target > tree.value:
	return helper(tree.right,target,curr)
    else:
	return curr
