class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        while s:
            stack.append(s.pop(0))
        while stack:
            s.append(stack.pop())
        