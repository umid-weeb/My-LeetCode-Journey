class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res = [0]*n
        stack =[]
        for i , num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                index = stack.pop()
                res[index]  = i - index
            stack.append(i)
        return res