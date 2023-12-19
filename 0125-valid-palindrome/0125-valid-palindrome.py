class Solution:
    def isPalindrome(self, s: str) -> bool:
    ##### Reverse String & compare
    ##### Time: O(n), space:O(n)
    # Sol1:
        # newStr = ""
        # for c in s:
        #     if c.isalnum():  # or if c.isalpha() or c.isdigit():
        #         newStr += c.lower()
        # return newStr == newStr[::-1]
    #Sol2:
        # filterS = filter(lambda c:c.isalnum(), s)
        # lowerS = map(lambda c:c.lower(), filterS)
        # filterS = list(lowerS)
        # return filterS == filterS[::-1]

    ##### Two pointers
    ##### Time: O(n), space:O(1)
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower(): return False
            l, r = l+1, r-1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9')
                )
