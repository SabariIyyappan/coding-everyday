class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)

        res = int((n*(n+1))/2) - sum(nums)

        return res
