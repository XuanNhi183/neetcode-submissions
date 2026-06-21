class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram={}
        for i in range (len(strs)):
            key="".join(sorted(strs[i]))
            if key in anagram:
                anagram[key].append(strs[i])
            else:
                anagram[key] = [strs[i]]
        return list(anagram.values())