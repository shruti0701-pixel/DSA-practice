class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        nums = Counter (nums)
        for key,value in nums.items():
            if value == 2:
                ans.append(key)
        return ans