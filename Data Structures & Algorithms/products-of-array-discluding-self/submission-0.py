class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    # i (i+1) (n-1) n

    # FINAL: ( (i+1)(n-1)n i(n-1)n i(i+1)n i(i+1)(n-1) )


    # L->R: (    1          i       i(i+1)  i(i+1)(n-1) )
    # R-L: ( (i+1)(n-1)n    (n-1)n  n       1   )

        L = [1 for _ in range(len(nums))]
        R = [1 for _ in range(len(nums))]

        for i in range(1,len(nums), 1):
            L[i] = nums[i-1]*L[i-1]
        
        print(L)

        for i in range(len(nums)-2, -1, -1):
            R[i] = nums[i+1]*R[i+1]
        
        print(R)

        result = [i*j for i,j in zip(R,L)]
        return result

    