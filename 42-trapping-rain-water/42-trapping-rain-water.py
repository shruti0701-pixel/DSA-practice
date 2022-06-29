class Solution:
    def trap(self, height: List[int]) -> int:
        left , right = 0 , len(height) - 1
        leftmax = rightmax = storewater = 0
        
        while left < right:
            leftmax = max(leftmax , height[left])
            rightmax = max(rightmax , height[right])
            
            if height[left] <= height[right]:
                storewater += leftmax - height[left]
                left += 1
            else:
                storewater += rightmax - height[right]
                right -= 1
        return storewater