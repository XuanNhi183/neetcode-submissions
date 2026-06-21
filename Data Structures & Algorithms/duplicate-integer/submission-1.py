class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        not_dupli=set(nums)
        return len(not_dupli) < len(nums)
             