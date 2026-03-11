class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res = [0]*n
        stack =[]
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index]  = i - prev_index
            stack.append(i)
        return res