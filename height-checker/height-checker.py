class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(0,len(heights)):          #for j in range(0 , len(expected)):
            if heights[i] == expected[i]:
                    i += 1
            else:
                count += 1
        return count
            
    