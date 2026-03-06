class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        umidA= sum(aliceSizes)
        umidB= sum(bobSizes)
        
        diff= (umidB-umidA)//2

        umidSet = set(bobSizes)
        for x in aliceSizes:
            y = x + diff
            if y in umidSet:
                return [x, y]