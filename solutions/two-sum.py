class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(0, len(nums)):
            a=nums[i]
            for j in range(i+1, len(nums)):
                if(a + nums[j] == target):
                    return [i, j]
