class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums))]

        d = dict()

        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        
        for n,f in d.items():
            buckets[f-1].append(n)

        result = list()
        while k > 0 and buckets != []:
            last = buckets.pop()

            while k > 0 and last != []:
                result.append(last.pop())
                k -= 1
        
        return result 
