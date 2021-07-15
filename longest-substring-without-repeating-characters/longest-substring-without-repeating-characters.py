class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_dist = 0
        fifo = []
        for s_ in s:
            if s_ not in fifo:
                fifo.append(s_)
                q_l = len(fifo)
                max_dist = len(fifo) if q_l > max_dist else max_dist
            else:
                while(1):
                    out = fifo.pop(0)
                    if out == s_:
                        break
                fifo.append(s_)
        return max_dist
