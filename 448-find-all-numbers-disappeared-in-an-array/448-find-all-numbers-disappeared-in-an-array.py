class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = Counter(nums)
        store = []
        for i in range(1 , len(nums) + 1):
            if i not in a:
                store.append(i)
        return store
        
        