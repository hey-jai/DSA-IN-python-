class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
            
        x = 1 
        while x <= n:
            if x == n:
                return True
            x = x * 3 
            
        return False
