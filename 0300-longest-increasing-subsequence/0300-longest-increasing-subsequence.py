import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return []
        tails = []
        tails_indices = []
        perent = [-1]* len(nums)

        for i, num in enumerate(nums):
            indx = bisect.bisect_left(tails, num)

            if indx == len(tails):
                tails.append(num)
                tails_indices.append(i)

            else:
                tails[indx] = num
                tails_indices[indx] =i



            if indx >0:
                perent[i] = tails_indices[indx -1]

        result = []
        current = tails_indices[-1]
        while current != -1:
            result.append(nums[current])
            current = perent[current]
        return len(result)


        