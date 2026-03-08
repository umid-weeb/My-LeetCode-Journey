from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            counter = Counter(word)
            key = frozenset(counter.items())
            group[key].append(word)
        return list(group.values())