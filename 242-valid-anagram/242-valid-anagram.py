class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #defaultdic
        
        if len(s) != len(t): return False
        
        count = collections.defaultdict(int)
        for i in s:
            count[i] += 1
        for i in t:
            count[i] -= 1
            if count[i] < 0:
                return False
        return True