class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_map = {}
        parent = [i for i in range(len(accounts))]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            p_x, p_y = find(x), find(y)
            if p_x == p_y:
                return
            parent[p_y] = p_x

        for account_idx in range(len(accounts)):
            for email_idx in range(1, len(accounts[account_idx])):
                email = accounts[account_idx][email_idx]
                print(email)
                if email in email_map:
                    union(email_map[email], account_idx)
                email_map[email] = parent[account_idx]
        
        groups = defaultdict(set)
        for i in range(len(accounts)):
            root = find(i)
            groups[root].update(accounts[i][1:])

        result = []
        for root, emails in groups.items():
            result.append([accounts[root][0]] + sorted(emails))
        return result


        # for i in range(len(accounts)):
        #     find(i)
        
        # res = [[accounts[i][0]] for i in email_map.values()]
        # for email in email_map.keys():
        #     # print(email)
        #     res[email_map[email]].append(email)
        # return res

        
        
        
        
        
        
        # parents = [i for i in range(len(accounts))]
        # name_same = defaultdict(list)
        # for i in range(len(accounts)):
        #     name_same[accounts[i][0]].append(i)
        
        # def find(x):
        #     if parent[x] != x:
        #         parent[x] = find(parent[x])
        #     return parent[x]
        
        # def union(x, y):
        #     p_x, p_y = find(x), find(y)
        #     if p_x == p_y:
        #         return
        #     a_y = set(accounts[y])
        #     for i in range(1, len(accounts[x])):
        #         if i in a_y:
        #             parent[p_y] = p_x
        #             return

        # for idxes in name_same.values():
        #     for i in range(len(idxes)):
        #         for j in range(i):
        #             union(idxes[i], idxes[j])
        
        # for i in range(len(accounts)):
        #     find(i)
