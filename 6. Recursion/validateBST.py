# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return helper(tree,float("-inf"),float("inf"))

def helper(tree,minv,maxv):
    if tree is None:
	return True
    if tree.value < minv or tree.value >=maxv:
	return False
    left = helper(tree.left,minv,tree.value)
    return left and helper(tree.right,tree.value,maxv)
