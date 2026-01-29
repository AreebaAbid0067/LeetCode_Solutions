class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        pos = [i for i in range(len(s)) if s[i] == c]
        res = []

        for i in range(len(s)):
            res.append(min(abs(i - p) for p in pos))

        return res