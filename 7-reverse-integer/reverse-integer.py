class Solution:
    def reverse(self, x: int) -> int:
        revCopy = x
        x = abs(x)
        revNum = 0
        while x > 0:
            lastDigit = x % 10
            revNum = revNum * 10 + lastDigit
            x = x // 10
        
        limit = 2 ** 31
        if revNum < -limit or revNum > limit:
            return 0
        return -revNum if revCopy < 0 else revNum 
