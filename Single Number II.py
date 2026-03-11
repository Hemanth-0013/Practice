class Solution(object):
    def singleNumber(self, nums):
        from collections import Counter
        c = Counter(nums)
        return next(key for key, value in c.items() if value == 1)
        
