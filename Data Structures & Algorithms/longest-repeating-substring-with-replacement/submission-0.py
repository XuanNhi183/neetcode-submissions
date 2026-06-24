from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        answer=0
        left=0
        window=dict()
        count=Counter()
        for right in range (len(s)):
            count[s[right]] += 1
            max_freq=max(count.values())
            while (right-left+1-max_freq) > k:
                count[s[left]] -= 1
                left += 1
            answer = max(answer, right-left+1)
        return answer
            