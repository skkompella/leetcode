class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        equality = []
        inequality = []
        for s in equations:
            if s[1] == '!':
                inequality.append(s)
            else:
                equality.append(s)

        for s in equality:
            x = s[0] 
            y = s[3]
            p_x, p_y = find(x), find(y)
            if p_x != p_y:
                parent[p_y] = p_x
        
        for s in inequality:
            x = s[0] 
            y = s[3]
            p_x, p_y = find(x), find(y)
            if p_x == p_y:
                return False
        return True


        # for s in equations:
        #     x = s[0] 
        #     y = s[3]
        #     rel = s[1:3]
        #     # print(rel)
        #     if x in parent and y in parent:
        #         p_x, p_y = find(x), find(y)
        #         if rel == '==':
        #             if p_x != p_y: # parents not the same
        #                 # print(p_x, p_y)
        #                 return False
        #         else:
        #             if p_x == p_y: # parents are the same
        #                 return False
        #     elif x not in parent and y in parent:
        #         if rel == '==':
        #             parent[x] = find(y)
        #         else:
        #             parent[x] = x
        #     elif y not in parent and x in parent:
        #         if rel == '==':
        #             parent[y] = find(x)
        #         else:
        #             parent[y] = y
        #     else:
        #         if rel == '==':
        #             parent[x] = x
        #             parent[y] = x
        #         else:
        #             if x == y:
        #                 return False
        #             parent[x] = x
        #             parent[y] = y
        
        # return True
                
                

