class Solution:
    def scoreOfString(self, s: str) -> int:
        curr_sum=0
        res=0
        for i in range (len(s)-1):
            curr_sum=abs(ord(s[i]) - ord(s[i+1]))
            res=res+curr_sum
        return res






        