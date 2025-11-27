class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #solution 1

        # charSet = set()
        # l = 0
        # res = 0
        # for r in range(len(s)):
        #     while s[r] in charSet:
        #         charSet.remove(s[l]) #jab tak s[r] found in charset we remove it

        #         l += 1  #length moves 1 point forward

        
        #     charSet.add(s[r])  #adding from the 0th index of the string
        #     res = max(res, r-l+1)

        #     # res = 3 

        # return res


        #solution 2  mam imama
        #we check within a substring if there are no repeating characters and we have to find the longest one 
        # n=len(s)
        # max_len=0
        # cset=set()
        # left=0
        h=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in h:
                h.remove(s[l])
                l+=1
            h.add(s[r])
            res=max(res,r-l+1)  #can also do len(set) this line is calculating the length of the set basically
        return res









          