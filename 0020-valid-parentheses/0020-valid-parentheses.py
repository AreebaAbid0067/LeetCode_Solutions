class Solution:
    def isValid(self, s: str) -> bool:
        # approach 1
        # stack = []
        # openToCLose = { "}": "{", "]": "[" ,")":"("}

        # for c in s:
        #     if c in openToCLose:
        #         if  stack and stack[-1] == openToCLose[c]:  #stack [-1] means accesssing top element
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(c)

        # return True if not stack else False

        # approach 2
        stack = []
        start = "([{"
        end = ")]}"
        for i in s:
            if i in start:
                stack.append(i)

            elif i in end:
                if stack and stack[-1] == start[end.index(i)]:
                    stack.pop()

                else:
                    return False

        return len(stack) == 0


        


