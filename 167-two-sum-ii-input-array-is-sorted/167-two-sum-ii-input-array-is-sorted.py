class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # as the array is sorted we are going to take two pointer approach
        left , right = 0 , len(numbers) - 1
        
        while left <= right:
            sums = numbers[left] + numbers[right]
            
            if sums == target:
                break
            elif sums >= target:
                right -= 1
            else:
                left += 1
        return [left+1,right + 1]
                
            
            
            
            
            
            
            
            
            
            