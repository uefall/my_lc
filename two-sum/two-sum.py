# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_d = {}
        for idx, num in enumerate(nums):
            if target-num in check_d:
                return [idx, check_d[target-num]]
            else:
                check_d[num] = idx
