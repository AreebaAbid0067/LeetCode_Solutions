class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # how to store count of each number?
        # in 2 pointers that would be then O(n^2) as for every one pointer it would have to 
        # check the whole array for repetition

        # set? no how would u check which one got removed
        # stack? 
        # make another array that stores the elements of the present array and one loop runs on first array and another on original to check if both values are the same

        """Correct approach is to use bit manipulation...convert all numbers to bit repr
        esentations and perform XOR operation on them"""

        res = 0  # n ^ 0 = n....^ here means XOR
        for n in nums:
            res = res ^ n

        return res