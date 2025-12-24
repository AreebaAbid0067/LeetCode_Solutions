class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    # Pointer for the next position to place the non-val elements
        j = 0
    
    # Iterate through the array
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        
        # The new length is j, as j points to the first position after the last valid element
        return j
    