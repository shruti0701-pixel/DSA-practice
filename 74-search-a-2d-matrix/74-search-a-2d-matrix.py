class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for num in matrix:
            if num[0] > target:
                break
            if num[-1] < target:
                continue
            
            low , high = 0 , len(num) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if num[mid] == target:
                    return True
                elif num[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return False