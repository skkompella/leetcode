class Solution:
    def intToRoman(self, num: int) -> str:
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        res = []
        for value, symbol in value_symbols:
            if num == 0:
                break
            count = num // value
            r = num - count * value
            res.append(count*symbol)
            num = r
        out = ''
        for i in res:
            out+=i
        return out


        # def recurse(r, prev, cnt): # remainder is string
        #     remainder = str(r)
        #     if (remainder[0] != '4' or remainder[0] != '9') and (pre):
        #         if r == 0:
        #             return ""
        #         elif r >= 1000:
        #             return "M" + recurse(r-1000)
        #         elif r >= 500:
        #             return "D" + recurse(r-500)
        #         elif r >= 100:
        #             return "C" + recurse(r-100)
        #         elif r >= 50:
        #             return "L" + recurse(r-50)
        #         elif r >= 10:
        #             return "X" + recurse(r-10)
        #         elif r >= 5:
        #             return "V" + recurse(r-5)
        #         elif r >= 1:
        #             return "I" + recurse(r-1)
        #     else:
        #         if r >= 500:
        #             return recurse(1000-r) + recurse(1000)
        #         elif r >= 100:
        #             return recurse(500-r) + recurse(500)
        #         elif r >= 50:
        #             return recurse(100-r) + recurse(100)
        #         elif r >= 10:
        #             return recurse(50-r) + recurse(50)
        #         elif r >= 5:
        #             return recurse(10-r) + recurse(10)
        #         elif r >= 1:
        #             return recurse(5-r) + recurse(5)
        # return recurse(num)
