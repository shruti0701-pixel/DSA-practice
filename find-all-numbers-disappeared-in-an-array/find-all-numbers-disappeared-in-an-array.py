class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = Counter(nums)
        storage = []
        for i in range(1 ,len(nums) + 1):
            if i not in a:
                storage.append(i)
        return storage