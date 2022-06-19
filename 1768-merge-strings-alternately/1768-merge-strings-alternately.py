class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = ""
        a = len(word1)
        b = len(word2)
        n = max(a,b)
        for i in range(n):
            if a > i:
                final += word1[i]
            if b > i:
                final += word2[i]
        return final    