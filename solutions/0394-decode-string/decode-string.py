class Solution:
    def decodeString(self, s: str) -> str:
        s = s+']'
        it = iter(range(len(s)))
        def decode():
            out_string = ''
            num = 0
            for i in it:
                char = s[i]
                if char.isdigit():
                    num = num * 10 + int(char)
                elif char == '[':
                    string = decode()
                    # print(num, string)
                    # print(num*string)
                    out_string += num * string
                    num=0
                elif char == ']':
                    print(out_string)
                    return out_string
                else:
                    # print(char)
                    out_string += char
                    # print(out_string)
        return decode()

        # # out = ''
        # s = s + ']'
        # def basecase(idx, num):
        #     nonlocal s
        #     out_string = ''
        #     print(num)
        #     for i in range(num):
        #         j = idx
        #         while True: # check if number or parentheses
        #             # print(j, s[j])
        #             if s[j] == ']':
        #                 j += 1
        #                 break
        #             # print(ord(s[j]))
        #             if ord(s[j]) >= 48 and ord(s[j]) <= 57: # if number
        #                 # print(j, s[j])
        #                 num = int(s[j])
        #                 while ord(s[j+1]) >= 48 and ord(s[j+1]) <= 57:
        #                     j += 1
        #                     num = num * 10 + int(s[j])
        #                 out_string += basecase(j+2, num)
        #                 print(j, s[j])
        #                 while s[j] != ']':
        #                     j += 1
        #                 j += 1

        #                 continue
        #             # if s[j] != '[':
        #             out_string += s[j] #character otherwise
        #             j += 1
        #     return out_string
        # return basecase(0, 1)
                    
