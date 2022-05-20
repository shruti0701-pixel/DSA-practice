class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low , high = 0 , int(math.sqrt(c))
        while low <= high:
            a = low * low
            b = high * high 
            if (a + b == c):
                return True
            elif (a + b > c):
                high -= 1
            elif (a + b < c):
                low += 1
        return False