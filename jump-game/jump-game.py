class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_pos = 0
        far_pos = nums[0]
        end_pos = len(nums)-1
        if far_pos >= end_pos:
            return True
        while(cur_pos < far_pos):
            cur_pos+=1
            tmp_far = cur_pos + nums[cur_pos]
            far_pos = tmp_far if tmp_far > far_pos else far_pos
            if far_pos >= end_pos:
                return True
        return False
