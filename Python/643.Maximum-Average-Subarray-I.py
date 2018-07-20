# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. 
# And you need to output the maximum average value.
# 
# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
# 
# Note:
# 1. 1 <= k <= n <= 30,000.
# 2. Elements of the given array will be in the range [-10,000, 10,000].



# 给定n个整数，找出平均数最大且长度为k的连续子数组，并输出该最大平均数。
# 
# 示例
# 输入: [1, 12, -5, -6, 50, 3], k = 4
# 输出: 12.75
# 解释: 最大平均数(12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# 
# 注意:
# 
# 1 <= k <= n <= 30, 000。
# 所给数据范围[-10, 000，10, 000]。


# 从头开始，先把最开始的k个数相加，然后向后移动，加上后面一个，减掉前面一个；然后每次判断最大值

class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        res = sum(nums[0:k])
        temp = res
        for i in range(k,len(nums)):
            temp = temp-nums[i-k]+nums[i]
            res = max(res, temp)
        return res/k
