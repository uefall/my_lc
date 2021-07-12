class Solution:
    def romanToInt(self, s: str) -> int:
        map_d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        spec_d = {'IV':-1,'IX':-1,'XL':-10,'XC':-10,'CD':-100,'CM':-100}
        rl = len(s)
        if rl < 2:
            return map_d[s]
        num = 0
        for i in range(len(s)-1):
            if s[i:i+2] in spec_d:
                num += spec_d[s[i:i+2]]
            else:
                num += map_d[s[i]]
        num += map_d[s[-1]]
        return num