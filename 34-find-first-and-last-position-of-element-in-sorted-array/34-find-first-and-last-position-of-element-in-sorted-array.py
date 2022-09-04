class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ele1 = -1
        low , high = 0 , len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                ele1 = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                
        ele2 = -1
        low , high = 0 , len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                ele2 = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return [ele1 , ele2]
                
    
                
        