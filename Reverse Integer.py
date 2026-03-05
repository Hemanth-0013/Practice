class Solution(object):
    def reverse(self, x):

        sign  = -1 if x < 0 else 1

        rev = int(str(abs(x))[::-1])

        if abs(rev) > 2**31:
            return 0

        return rev * sign
