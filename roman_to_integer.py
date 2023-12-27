"""
Runtime: 51 ms (98.36%)
Memory 18.7 MB (6.9%)
"""

class Solution:
    def roman_to_int(self, s: str) -> int:
        replacements = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i + 2] in replacements:
                result += replacements[s[i:i + 2]]
                i += 2
            else:
                result += replacements[s[i]]
                i += 1

        return result

# Test cases
print(Solution().roman_to_int("III"))
print(Solution().roman_to_int("LVIII"))
print(Solution().roman_to_int("MCMXCIV"))
