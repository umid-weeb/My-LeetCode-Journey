class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        count = [0] * 26

        for c in magazine:
            count[ord(c) - ord('a')] += 1

        for c in ransomNote:
            idx = ord(c) - ord('a')
            count[idx] -= 1
            if count[idx] < 0:
                return False

        return True