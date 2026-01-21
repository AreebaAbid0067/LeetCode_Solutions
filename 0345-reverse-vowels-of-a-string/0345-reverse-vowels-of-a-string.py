class Solution:
    def reverseVowels(self, s: str) -> str:
        ans = list(s)
        # we need to convert the string to array so that its iterable
        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        left , right = 0, len(ans) - 1
        while left < right:
            if ans[left] not in vowels:
                left += 1

            elif ans[right] not in vowels:
                right -= 1

            else:
                ans[left], ans[right] = ans[right], ans[left]
                left += 1
                right -= 1

        return "".join(ans) # now converting the array to string 
