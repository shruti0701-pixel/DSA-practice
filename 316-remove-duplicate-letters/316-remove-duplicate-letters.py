class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        index = {c:i for i,c in enumerate(s)}
        stack = []
        
        for i,c in enumerate(s):
            if c not in stack:
                while stack and stack[-1] > c and index[stack[-1]] > i:
                    stack.pop()
                stack.append(c)
        return ''.join(stack)
            