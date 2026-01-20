class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # the sets approach
        s = set(nums)
        if len(s) == len(nums): # means no duplicates in nums..bcz distinct in nums and set
            return False
        else:
            return True
