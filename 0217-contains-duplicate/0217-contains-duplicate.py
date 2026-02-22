class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result_set = set(nums)
        if len(result_set) == len(nums): #means if there were duplicates in nums array, then result_set would contain less numbers so less in length
            return False

        else:
            return True
