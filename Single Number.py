class Solution(object):
    def singleNumber(self, nums):
        from collections import Counter

        a = Counter(nums)

        return next(key for key, value in a.items() if value == 1)
