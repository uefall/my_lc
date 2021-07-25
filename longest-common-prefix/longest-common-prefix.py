class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        self.re = None
        for str_ in strs:
            # print(str_)
            break_flg = False
            if not self.re:
                self.re = str_
                self.l = len(self.re)
            else:
                for idx,s in enumerate(str_):
                    if idx >= self.l:
                        break_flg = True
                        break
                    if s != self.re[idx]:
                        self.re = str_[:idx]
                        self.l = len(self.re)
                        # print('update',self.re, self.l)
                        break_flg = True
                        break
            if not break_flg:
                # print('hh',self.l)
                self.re = str_ if len(str_) < self.l else self.re
                self.l = len(self.re)
            if self.l == 0:
                return self.re
            # print('re',self.re)
        return self.re
                        