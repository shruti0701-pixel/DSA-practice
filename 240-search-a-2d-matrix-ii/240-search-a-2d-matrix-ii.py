class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(nums , target):
            low , high = 0 , len(nums)
            while low < high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    high = mid
                elif nums[mid] < target:
                    low = mid + 1
            return False
        
        for row in matrix:
            if binarySearch(row , target):
                return True
        return False
            