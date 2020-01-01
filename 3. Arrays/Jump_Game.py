
def canJump(self, nums: List[int]) -> bool:
    best=0
    for i in range(len(nums)):
        if best < i:
            return False
        best = max(best,nums[i]+i)
    return True
