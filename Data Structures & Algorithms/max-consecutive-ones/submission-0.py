class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        m = 0
        c = 0
        for e in nums:
            if e == 1:
                c += 1
                m = max(m, c)
            if e != 1:
                c = 0
        
        return m