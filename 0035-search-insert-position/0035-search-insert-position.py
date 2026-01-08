class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left , right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return left

        # when the loop ends the left moves to the index which is supposed to contain the target number
        # in the case of example 2 specifically