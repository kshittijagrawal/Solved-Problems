class Solution:
    def strStr(self, haystack, needle):
        if len(needle) > len(haystack):
            return -1
        elif needle == haystack:
            return 0
        else:
            for i in range(len(haystack)):
                if haystack[i:i+len(needle)] == needle:
                    return i
            return -1