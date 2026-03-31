class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        
        for idx, val in enumerate(nums):
            d[val] = idx

        for idx, val in enumerate(nums):
            diff = target - val

            if diff in d and d[diff] != idx:
                return [idx, d[diff]]