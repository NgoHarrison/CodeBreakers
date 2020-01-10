class Solution:
    def searchRange(self, nums, target):
        if len(nums)==0:
            return [-1,-1]
        lst = [i for (i,x) in enumerate(nums) if x==target]
        
        if not lst:
            return [-1,-1]
        return [lst[0],lst[len(lst)-1]]
