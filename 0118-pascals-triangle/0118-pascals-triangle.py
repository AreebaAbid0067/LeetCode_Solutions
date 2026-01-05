class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # time complex: O(n^2)...n is the number of rows here
        res = [[1]]
        for i in range(numRows-1): # as we already added one row earlier in the res
            temp=[0] + res[-1] + [0] #to the previous row add zero before and one zero after
            row = []
            for j in range(len(res[-1]) + 1):

                row.append(temp[j] + temp[j+1])

            res.append(row)

        return res



         