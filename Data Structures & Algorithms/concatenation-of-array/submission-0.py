class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concat=[]
        for i in range(len(nums)*2):
            concat.append(nums[i%len(nums)])
        return concat


        