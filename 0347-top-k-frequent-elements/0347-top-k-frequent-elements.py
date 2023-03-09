class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1      
        sorted_frequency = {k: v for k, v in sorted(frequency.items(), key=lambda item: item[1], reverse=True)}
        return_arr = []
        for i, (p, v) in enumerate(sorted_frequency.items()):
            if i >= k:
                break
            return_arr.append(p)
        return return_arr