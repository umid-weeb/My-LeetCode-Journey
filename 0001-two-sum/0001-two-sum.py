class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, qiymat in enumerate(nums):
            need = target - nums[i]

            if need in seen:
                return [i, seen[need]]
            else:
                seen[qiymat] = i
