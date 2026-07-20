class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ip_split = queryIP.split('.')
        if len(ip_split) == 4:
            for i in range(4):
                jon = None
                try:
                    jon = (int)(ip_split[i])
                except:
                    return "Neither"              
                if (jon == 0 and ip_split[i] != '0') or (not (0 <= jon <= 255)) or (jon != 0 and ip_split[i][0] == '0'):
                    return "Neither"
            return "IPv4"
        ip_split = queryIP.split(':')
        # ip_v6_map = {
        #     '0':1, '1':1, '2':1, '3':1, '4':1, '5':1, '6':1, '7':1, '8':1, '9':1, 
        #     'a':1, 'b':1, 'c':1, 'd':1, 'e':1, 'f':1, 
        #     'A':1, 'B':1, 'C':1, 'D':1, 'E':1, 'F':1, }
        if len(ip_split) == 8:
            for i in range(8):
                if 0 < len(ip_split[i]) <= 4:
                    for j in ip_split[i]:
                        asci = ord(j)
                        if not ((48 <= asci <= 57) or (65 <= asci <= 70) or (97 <= asci <= 102)):
                            return "Neither"
                else:
                    return "Neither"
            return "IPv6"
        return "Neither"
                
