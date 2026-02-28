class Solution(object):
    def isAnagram(self, s, t):
        
        # approach 1 using hasmaps to count the occurence of each character in s and t
        if len(s) != len(t):
            return False

        countS, countT = {} , {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for char in s:
            if countS[char] != countT.get(char,0):
                return False

        return True
        