class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = dict()

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if nums[i] in temp:
                return [temp[nums[i]], i]

            temp[diff] = i


