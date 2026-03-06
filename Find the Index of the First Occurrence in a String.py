class Solution(object):
    def strStr(self, haystack, needle):
        n = len(haystack)
        m = len(needle)
        
        

        for i in range(n - m + 1):
            if needle in haystack[i : i + m]:
                return i
        
        return -1
