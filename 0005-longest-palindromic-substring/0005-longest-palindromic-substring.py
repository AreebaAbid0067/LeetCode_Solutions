class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Helper function to expand around the center
        def expandAroundCenter(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the longest palindromic substring
            return s[left + 1:right]

        if not s or len(s) == 1:
            return s
        
        longest = ""
        
        for i in range(len(s)):
            # Check for odd length palindromes
            odd_palindrome = expandAroundCenter(s, i, i)
            # Check for even length palindromes
            even_palindrome = expandAroundCenter(s, i, i + 1)
            
            # Find the longest palindrome
            longest = max(longest, odd_palindrome, even_palindrome, key=len)
        
        return longest