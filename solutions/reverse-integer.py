class Solution:
    def reverse(self, x: int) -> int:
        
        
        out = ""
        
        if (x > 0):
            s = str(x)
            for i, a in enumerate(reversed(s)):
                out = out + a
        
            if(int(out) < ((pow(2,31)) - 1)):
                return int(out)
            else:
                return 0
        else:
            x = x*-1
            
            s = str(x)
            for i, a in enumerate(reversed(s)):
                out = out + a
        
            if(-1*int(out) > (-(pow(2,31)))):
                return -1*int(out)
            else:
                return 0
