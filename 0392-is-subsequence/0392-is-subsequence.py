class Solution:
    def isSubsequence(self, sequence: str, text: str) -> bool:
        seq_ind=0
        seq_len = len(sequence)
        if not sequence:
            return True
        sequence_l = list(sequence)
        
        for i in text:
            if i == sequence_l[0]:
                sequence_l.pop(0)
                if len(sequence_l)==0:
                    return True
        return len(sequence_l)==0
                