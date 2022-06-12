class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        #sliding window problem
        uniqueele = set()
        maxsum = cursum = 0
        i = 0 #starting ptr
        for j in range(len(nums)): #ending pointer
            while nums[j] in uniqueele:
                cursum -= nums[i]
                uniqueele.remove(nums[i])
                i += 1
            uniqueele.add(nums[j])
            cursum += nums[j]
            maxsum = max(maxsum , cursum)
        return maxsum
            