class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_dist = 0
        fifo = []
        for s_ in s:
            if s_ not in fifo:
                fifo.append(s_)
                if len(fifo) > max_dist:
                    max_dist = len(fifo)
            else:
                while(1):
                    out = fifo.pop(0)
                    if out == s_:
                        break
                fifo.append(s_)
        return max_dist