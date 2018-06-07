
# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# My Method:
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        result = []
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result
                    
                  
# Improved Method：
'''判断target与某个元素的差值是否在列表中即可实现一层循环即解决问题'''
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        result = []
        for i in range(n):
            first = nums[i]
            second = target - first
            if second in nums:
                j = nums.index(second)
                if j != i:
                    result.append(i)
                    result.append(j)
                    return result
                   
