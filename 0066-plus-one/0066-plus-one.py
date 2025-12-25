class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # result = []
        # if len(digits) == 1:
        #     answer = digits[0] + 1
        #     result = [int(i) for i in str(answer)]
        #     return result
        

        # length = len(digits)
        # digits[length-1]  += 1
        # return digits


        "Neetcode Solution"
        digits = digits[::-1] # reverse the array
        one, i = 1,0
        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0

                else:
                    digits[i] += 1 # if not 9 we wont have a carry
                    one = 0

            else:
                digits.append(1)
                one = 0

            i += 1
        return digits[::-1]

        