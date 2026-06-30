class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count={}
        i=0
        for num in nums:
            count[num] = count.get(num,0)+1
        for color in [0,1,2]:
            for _ in range (count.get(color, 0)):
                nums[i] = color
                i+=1
        return
            



        