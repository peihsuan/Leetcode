class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, num in enumerate(nums):
            other_num = target - num
            if other_num in nums[index+1:]:
                other_num_index = nums[index+1:].index(other_num) + index + 1
                return index, other_num_index
