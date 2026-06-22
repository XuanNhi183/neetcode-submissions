class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=sorted(nums)
        current_len=1
        longest_len = 1
        i=1
        while i<len(nums):
            if nums[i] == nums[i-1]:
                i+=1
                continue
            if nums[i] == nums[i-1]+ 1:
                current_len+=1
            else:
                current_len = 1
            longest_len = max(longest_len,current_len)
            i+=1
        return longest_len
