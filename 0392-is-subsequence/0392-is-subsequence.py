class Solution:
    def isSubsequence(self, sequence: str, text: str) -> bool:
        seq_ind=0
        seq_len = len(sequence)
        if not sequence:
            return True
        
        for i in text:
            if i == sequence[seq_ind]:
                seq_ind+=1
                if seq_ind == seq_len:
                    return True
        return False
            
        
        