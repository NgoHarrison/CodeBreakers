class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev = nums[0]
        pointer = 1
        while pointer < len(nums):
            while nums[pointer]==prev:
                nums.pop(pointer)
                if pointer >= len(nums):
                    return len(nums)
            prev = nums[pointer]
            pointer+=1
            
        return len(nums)
