class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pair:[temp, index] index so we can calc diff

        for i, t in enumerate(temperatures):
            #while stack is empty and temo gretaer than top of stack
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                #modify value in res array at stackInd based on diff
                res[stackInd] = (i - stackInd)
            #if no greater value then just append
            stack.append([t, i])
        return res
            