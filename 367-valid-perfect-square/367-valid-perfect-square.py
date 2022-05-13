class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low , high = 0 , num
        while low <= high:
            mid = low + (high - low) // 2
            sqrt = mid * mid
            if sqrt == num:
                return True
            elif sqrt > num:
                high = mid - 1
            else:
                low = mid + 1
        return False
                