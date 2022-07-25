class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for i in nums:
            if 0 in nums:
                return 0
            product *= i
        if product < 0:
            return -1
        else:
            return 1