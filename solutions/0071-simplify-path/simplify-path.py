class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        i = 0
        while i < len(path_list):
            # print(path_list)
            if path_list[i] == '' or path_list[i] == '.':
                del path_list[i]
            elif path_list[i] == '..':
                del path_list[i]
                if i > 0:
                    del path_list[i-1]
                    i -= 1
            else:
                i+=1
        # print(path_list)
        res = ''
        for el in path_list:
            if el:
                res+='/'
                res+=el
        if not res:
            return '/'
        return res
                
