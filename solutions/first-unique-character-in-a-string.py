class Solution:
    def firstUniqChar(self, s: str) -> int:
        dicts = {}
        for i, char in enumerate(s):
            if char not in dicts:
                dicts[char] = 1    
            else:
                dicts[char] += 1
        
        for i, char in enumerate(s):
            
            if(dicts[char] == 1):
                return i
            
        return -1        
        
