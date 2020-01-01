class Solution:

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        start = 0
        prod = 1
        output = 0
        for i in range(len(nums)):
            prod*=nums[i]
            while prod >= k:
                prod/=nums[start]
                start +=1
                
            output+=i-start+1
            print(i, output)
        return output
            
