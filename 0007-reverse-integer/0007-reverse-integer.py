class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        # Get the absolute value and reverse it by converting to string
        rev_str = str(abs(x))[::-1]
        # Convert it back to an integer
        rev_int = int(rev_str)
        
        # Restore the sign if the original number was negative
        if negative:
            rev_int = -rev_int
        
        # Check if the result is within the 32-bit signed integer range
        if rev_int < -2**31 or rev_int > 2**31 - 1:
            return 0
        
        return rev_int