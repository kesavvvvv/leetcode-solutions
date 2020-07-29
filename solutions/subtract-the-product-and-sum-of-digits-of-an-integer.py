class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        prod = 1
        summ = 0
        for i, number in enumerate(str(n)):
            prod *= int(number)
            summ += int(number)
            
        return prod - summ  
