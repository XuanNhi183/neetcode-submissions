class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        maxLen=0
        words = s.split()
        return len(words[-1])
        

        