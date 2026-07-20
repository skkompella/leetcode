class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        letters = []
        s = '#'+s
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                letters.append([s[i], 0])
            letters[-1][1] += 1
        # print(letters)
        
        cnt = 0
        def parseword(word):
            nonlocal cnt
            word_letters = []
            word = '#'+word
            for i in range(1, len(word)):
                # if i not in letters[:][0]:
                #     return
                if word[i] != word[i-1]:
                    word_letters.append([word[i], 0])
                word_letters[-1][1] += 1
            
            # print(word_letters)
            if len(word_letters) != len(letters):
                return
            for i in range(0, len(word_letters)):
                ron = word_letters[i] # non stretchy letter
                jon = letters[i] # stretchy letter
                if ron[0] != jon[0]:
                    return
                if jon[1] < ron[1]:
                    return
                if (ron[1] < 3 and jon[1] < 3) and ron[1] != jon[1]:
                    return                
                # print(jon[1], ron[1])
                
            cnt += 1
            return
        for w in words:
            parseword(w)
        return cnt
