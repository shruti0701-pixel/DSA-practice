class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def binarySearch(row):
            low , high = 0 , len(row)
            while low < high:
                mid = low + (high - low) // 2
                if row[mid] < 0:
                    high = mid
                else:
                    low = mid + 1
            return len(row) - low
        
        count = 0
        for row in grid:
            count += binarySearch(row)
        return (count)