class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        last = []
        for i in range(len(nums)):
            res=0
            for j in range(0, i+1):
                res +=nums[j]
            last.append(res)
        return last
        