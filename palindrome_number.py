# problem #9

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False 
        else:
            y = str(x)[::-1]
        
        if(int(y) == x):
            return True
        else:
            False 