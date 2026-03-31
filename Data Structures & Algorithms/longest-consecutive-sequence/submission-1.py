class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums)
        l_max = 0


        for n in nums:
            if n-1 in s:
                continue
    
            l = []
            while n in s:
                l.append(n)
                n += 1
            
            l_max = max(l_max, len(l))

        return l_max