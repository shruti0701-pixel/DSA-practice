class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in range(0 , len(nums)):
            digit = 0
            a = nums[i]
            while (a > 0):
                digit += 1
                a = a//10
            if (digit%2 == 0):
                count += 1
        return count