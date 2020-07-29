class Solution:
    def removeDuplicates(self, S: str) -> str:
        
        for char in S:
            if char * 2 in S:
                S = S.replace(char*2, '')
                
        return S       
