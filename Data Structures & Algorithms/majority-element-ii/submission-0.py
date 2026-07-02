class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter=dict()
        res=[]
        for num in nums:
            counter[num] = counter.get(num,0)+1
            if counter[num] > len(nums)//3 and num not in res:
                res.append(num)
        return res
        