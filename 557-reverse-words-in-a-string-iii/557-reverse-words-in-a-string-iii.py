class Solution:
    def reverseWords(self, s: str) -> str:
        split_wrds = s . split(" ")
        split_wrds = [i[::-1] for i in split_wrds]
        return " ".join(split_wrds)