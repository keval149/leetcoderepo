class Solution:

    def helperValidPalin(self, st: str) -> bool:
        start = 0
        end = len(st) - 1
        while start < end:
            if st[start] != st[end]:
                return False
            start += 1
            end -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        st = 0
        en = len(s) - 1

        while st < en:
            if s[st] != s[en]:
                return self.helperValidPalin(s[st + 1:en + 1]) or self.helperValidPalin(s[st:en])
            st += 1
            en -= 1
        return True
s = "abca"
obj = Solution()
result = obj.validPalindrome(s)
print("Is {} a valid palindrome: {}".format(s,result))
