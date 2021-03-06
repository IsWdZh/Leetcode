# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] 
# and the absolute difference between i and j is at most k.
# 
# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true
# 
# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true
# 
# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false



# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。
# 
# 示例 1:
# 输入: nums = [1,2,3,1], k = 3
# 输出: true
# 
# 示例 2:
# 输入: nums = [1,0,1,1], k = 1
# 输出: true
# 
# 示例 3:
# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(set(nums)) == len(nums):
            return False
        else:
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    n = j-i
                    if nums[i] == nums[j] and n <= k:
                        return True
            return False
