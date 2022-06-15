class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return nums
        j = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[j] , nums[i] = nums[i] , nums[j]
                j += 1
        return nums    