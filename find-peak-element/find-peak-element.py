# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l_flg = True
        for idx, v in enumerate(nums):
            if idx == 0:
                last_v = v
            else:
                if v < last_v:
                    if l_flg:
                        return idx-1
                    l_flg = False
                else:
                    l_flg = True
                last_v = v
        return idx
