class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        not_duplicated=set(nums)
        return len(set(nums)) < len(nums)
        