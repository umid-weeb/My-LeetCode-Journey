from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_magazine = Counter(magazine)
        counter_ransom = Counter(ransomNote)

        for i , n in counter_ransom.items():
            if counter_magazine[i] <n:
                return False
        return True