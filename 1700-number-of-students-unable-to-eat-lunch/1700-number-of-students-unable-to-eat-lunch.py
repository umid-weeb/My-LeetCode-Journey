from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        counter  = Counter(students)
        for i in sandwiches:
            if counter[i]>0:
                res-=1
                counter[i]-=1
            else:
                return res
        return res