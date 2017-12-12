class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, item in enumerate(nums):
            otherNum = target - item
            if otherNum in nums[index+1:]:
                index2 = nums[index+1:].index(otherNum)+1+index
                return [index, index2]

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([3, 3], 6))
    print(sol.twoSum([1, 2, 4, 6], 6))
    print(sol.twoSum([0, 1, 2, 4, 6], 5))