# Given an integer array nums, find the contiguous subarray (containing at least one number) which has 
# the largest sum and return its sum.

# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Follow up:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 进阶:
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。


# 解析：设置一个局部最大值，一个全局最大值；从头遍历整个nums，不断更新local最大值，小于0则说明将前面的值均抛弃，所以仍令local最大值为0；
#       然后将所有时刻的local最大值存入global最大值；

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0:
            return max(nums)
        local_max, global_max = 0, 0
        for i in nums:
            local_max = max(0, local_max+i)
            global_max = max(local_max, global_max)
        return global_max
