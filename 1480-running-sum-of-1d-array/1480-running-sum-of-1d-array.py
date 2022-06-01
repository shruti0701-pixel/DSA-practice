class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [nums[0]]
        for i in range(1,len(nums)):
            nums[i] += nums[i - 1]
            output.append(nums[i])
        return output