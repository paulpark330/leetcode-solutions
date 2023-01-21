class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # { val: index }
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i
        return