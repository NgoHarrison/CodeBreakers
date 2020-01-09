def findMin(self, nums: List[int]) -> int:
    lo = 0
    hi = len(nums)-1
    if len(nums)==1:
        return nums[0]
    while lo <= hi:
        mid = (lo+hi)//2
        if nums[hi] > nums[lo]:
            return nums[lo]
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        if nums[mid-1] > nums[mid]:
            return nums[mid]
        if nums[mid] > nums[0]:
            lo = mid + 1
        else:
            hi = mid - 1
