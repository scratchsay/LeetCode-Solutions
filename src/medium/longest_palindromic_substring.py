class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        string = ""
        current_best = 0
        if s == s[::-1]:
            return s
        for i in range(n):
            for j in range(i+1,n):
                if s[(i-1):j] == s[(i-1):j][::-1]:
                    if current_best < len(s[i:j]):
                        current_best = len(s[i:j])
                        string = s[i:j]
        return string
