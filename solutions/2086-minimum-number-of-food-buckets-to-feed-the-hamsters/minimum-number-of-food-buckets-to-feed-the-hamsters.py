class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        # if len(hamsters) == 1 and hamsters == 'H': # 
        #     return -1
        ham_list = list(hamsters)
        length = len(ham_list)
        count = 0
        for i in range(length):
            if ham_list[i] == 'H':
                if i < length-1 and ham_list[i+1] == 'b':
                    continue 
                elif i > 0 and ham_list[i-1] == 'b':
                    continue
                elif i < length-1 and ham_list[i+1] == '.':
                    ham_list[i+1] = 'b'
                    count += 1
                elif i > 0 and ham_list[i-1] == '.':
                    ham_list[i-1] = 'b'
                    count += 1
                else:
                    return -1
        return count
                
