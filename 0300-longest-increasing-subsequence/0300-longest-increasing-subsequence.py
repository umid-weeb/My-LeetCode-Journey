# import bisect
def binary_search(tails, num):
    low, high = 0, len(tails)
    while low<high:
        mid = (low+high)//2
        if tails[mid]<num:
            low = mid +1
        else:
            high = mid
    return low


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = []
        for num in nums:
            idx = binary_search(temp, num)
            if idx<len(temp):
                temp[idx] = num
            else:
                temp.append(num)
        return len(temp)

        