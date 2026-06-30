class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        for num in nums:
            count[num] = count.get(num,0) +1
            # nếu num tồn tại trong count, trả về giá trị của nó,
            # ngược lại nếu ko có, trả về 0, +1 vào để tăng giá trị số lần
            if count[num] > len(nums)/2:
                return num


        