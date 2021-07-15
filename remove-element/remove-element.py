# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valid_pos = 0
        for num in nums:
            if num != val:
                nums[valid_pos] = num
                valid_pos += 1
        nums[valid_pos:] = '_'
        return valid_pos
