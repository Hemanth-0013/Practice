class Solution(object):
    def plusOne(self, digits):
        sum = 0

        for i in digits:
            sum = sum * 10 + i

        sum += 1

        return [int(d) for d in str(sum)]

        
