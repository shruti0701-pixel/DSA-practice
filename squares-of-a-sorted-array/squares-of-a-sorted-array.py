class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        low , high = 0 , len(nums) - 1
        sqrlst = []
        while low <= high:
            if (abs(nums[low]) > abs(nums[high])):
                sqrlst.append(nums[low] **2)
                low += 1
            else:
                sqrlst.append(nums[high] **2)
                high -= 1
        return reversed(sqrlst)