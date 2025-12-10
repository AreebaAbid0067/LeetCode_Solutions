class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1): # we write -1 to tell ourselves that two pointer approach is used
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return(i,j)
