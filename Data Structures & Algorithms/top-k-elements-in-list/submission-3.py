class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        result = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        result_list=[]
        for pair in result[:k]:
            result_list.append(pair[0])
        return result_list
                
        