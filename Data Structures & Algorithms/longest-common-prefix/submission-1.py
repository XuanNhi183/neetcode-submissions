class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range (len(prefix)):
            char = prefix[i]
            for j in range (1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return prefix[:i]       
        return prefix    
            

        