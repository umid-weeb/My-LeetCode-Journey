class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows =[
            set("qwertyuiop"),
            set('asdfghjkl'),
            set("zxcvbnm"),
        ]
        res=[]
        for word in words:
            w = set(word.lower())
            for row in rows:
                if w<=row:
                    res.append(word)
                    break
        return res