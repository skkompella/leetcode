class Solution:
    def romanToInt(self, s: str) -> int:
        roman = [("M", 1000), ("CM", 900), ("D", 500),("CD", 400),
                    ("C", 100),("XC", 90),("L", 50),("XL", 40),
                    ("X", 10),("IX", 9),("V", 5), ("IV", 4),("I", 1)]
        num = 0
        for letter, val in roman:
            if s == "":
                break
            if len(letter) == 1:
                while s != '' and s[0] == letter:
                    s = s[1:]
                    num += val
            elif len(letter) == 2:
                # print(s, s[:1], s[:2], s[2:])
                while s != '' and s[:2] == letter:
                    s = s[2:]
                    num += val
        return num
