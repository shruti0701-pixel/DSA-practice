class Solution:
    def climbStairs(self, n: int) -> int:
        x , y , z = 1 , 1 , 0
        for i in range(n):
            z =  x + y
            x = y 
            y = z
        return x