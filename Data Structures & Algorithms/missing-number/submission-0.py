class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = (len(nums)/2) * (len(nums) + 1)
        sums = 0
        for x in nums:
            sums += x
        return int(expected) - sums
        