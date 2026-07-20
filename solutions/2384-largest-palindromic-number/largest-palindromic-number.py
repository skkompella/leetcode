class Solution:
    def largestPalindromic(self, num: str) -> str:
        # make a set with each number + counts
        # for numbers with only 1 count, put the largest number in the middle
        # for numbers with 2 or more count, put the smallest number * (count // 2) on each side, then pop and repeat
        num_counts = collections.defaultdict()
        for i in num:
            if i not in num_counts:
                num_counts[i] = 0
            num_counts[i] += 1
        mid = ''
        left_wing = ''
        middle_number = -1
        for i in '9876543210':
            if i in num_counts:
                # if num_counts[i] == 1:
                #     if int(i) > middle_number:
                #         middle_number = int(i)
                # print(i, left_wing)
                if i == '0' and left_wing == '':
                    break
                count = num_counts[i] // 2
                left_wing += count * i
                num_counts[i] -= count * 2
        
        for i in '9876543210':
            if i in num_counts and num_counts[i] > 0:
                mid = i
                break
        

        # mid = ''
        # if middle_number != -1:
        #     mid = str(middle_number)
        return left_wing + mid + left_wing[::-1]

                     


        # max_1_count = '-1'
        # for i in num_counts.keys():
        #     if num_counts[i] == 1:
        #         if int(max_1_count) < int(i):
        #             max_1_count = i
        #         num_counts.pop(i)
        
        # res = ''
        # if max_1_count != '-1':
        #     res = max_1_count
        
        # while len(num_counts) != 0:
        #     num_counts.keys
        

        
