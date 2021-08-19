# problem #7 

class Solution:
    def reverse(self, x: int) -> int:
        
        # sign for negative value 
        sign = ''

        # check if x is negative 
        if(x < 0):
            x = abs(x)
            sign = '-'

        # convert int to string 
        x = str(x)

        length = len(x)
        # remove any trailing zeros if needed
        if length > 1:
            for i in range(0, length, 1):
                if(x[length - 1 - i] == '0'):
                    x = x[:-1]
                else:
                    break
        
        # reverse x
        x = sign + x[::-1]
        
        # check if x is in range 
        if(int(x) <= int(2**31 - 1) and int(x) >= int(-2**31)):
            return x
        else:
            return 0