class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        yigindi = sum(nums)
        left = 0
        for i, x in enumerate(nums):
            if left == (yigindi - left - x):
                return i
            left +=x
        return -1