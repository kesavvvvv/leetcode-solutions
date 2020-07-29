class Solution:
    def toGoatLatin(self, S: str) -> str:
        
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        words = S.split(" ")
        result = ""
        
        test = 1
        
        for i, word in enumerate(words):
            if word[0] in vowel:
                word = word + "ma"
                j = 0    
                while(j<test):
                    word = word + "a"
                    j += 1
                if(i != len(words) - 1):    
                    result = result + word + " "        
                else:
                    result = result + word
            else:
                word = word + word[0]
                word = word.replace(word[0], '', 1)
                word = word + "ma"
                j = 0    
                while(j<test):
                    word = word + "a"
                    j += 1
                if(i != len(words) - 1):    
                    result = result + word + " "        
                else:
                    result = result + word
            test += 1
            
        return result     
        
