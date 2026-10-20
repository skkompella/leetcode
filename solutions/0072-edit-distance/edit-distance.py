class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        word1len = len(word1)
        word2len = len(word2)

        def recurse(i, j): # where i is position for ith idx in word1 and j is jth idx in word2
            if i >= word1len and j >= word2len:
                return 0
            if i >= word1len and j <= word2len:
                return word2len-j
            if i <= word1len and j >= word2len:
                return word1len-i
            # print("goon")
            if (i, j) not in cache:
                # options: 
                # insert: i, j+1
                # delete: i+1, j
                # replace: i+1, j+1
                # same char: i+1, j+1, no penalty
                if word1[i] == word2[j]:
                    # cache[(i, j)]= min(recurse(i+1, j+1), 1+recurse(i, j+1), 1+recurse(i+1, j), 1+recurse(i+1, j+1))
                    cache[(i, j)]= recurse(i+1, j+1)
                else:
                    cache[(i, j)]= min(1+recurse(i, j+1), 1+recurse(i+1, j), 1+recurse(i+1, j+1))
            return cache[(i, j)]
        

        return recurse(0, 0)
        # tmp = recurse(0, 0)
        # if tmp == float('inf'):
        #     return 0
        # return tmp
