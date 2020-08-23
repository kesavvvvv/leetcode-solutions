class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        number = 0
        for i in range(len(digits) - 1, -1, -1):
            number += digits[i]*pow(10, len(digits) - i - 1)
        
        number += 1
        
        op = [0]*len(str(number))
        
        i=0
        for d in str(number):
            op[i] = int(d)
            i+=1
            
        return op    
