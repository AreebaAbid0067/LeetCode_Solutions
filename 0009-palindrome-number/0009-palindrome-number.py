class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
    
        # Step 2: Create a reversed version of the number
        original = x
        reversed_num = 0
        
        while x > 0:
            last_digit = x % 10
            reversed_num = reversed_num * 10 + last_digit
            x //= 10
        
        # Step 3: Compare the original number with the reversed number
        return original == reversed_num