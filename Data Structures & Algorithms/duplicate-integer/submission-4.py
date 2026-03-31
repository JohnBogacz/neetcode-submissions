class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hello = set()
        for letter in nums:
            if letter not in hello:
                hello.add(letter)
            else:
                return True

        return False