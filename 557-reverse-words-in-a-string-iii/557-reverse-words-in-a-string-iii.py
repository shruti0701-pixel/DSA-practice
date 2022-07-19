class Solution:
    def reverseWords(self, s: str) -> str:
        split_lst = s. split(" ")
        split_lst = [i[::-1] for i in split_lst]
        return " ".join(split_lst)