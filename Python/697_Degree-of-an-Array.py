# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
# 
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
# 
# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# 
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6
# 
# Note:
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.





# 给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
# 
# 你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
# 
# 示例 1:
# 输入: [1, 2, 2, 3, 1]
# 输出: 2
# 解释: 
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.
# 
# 示例 2:
# 输入: [1,2,2,3,1,4,2]
# 输出: 6
# 
# 注意:
# nums.length 在1到50,000区间范围内。
# nums[i] 是一个在0到49,999范围内的整数。



# 解析:
# 1. 首先将数组内的元素作为key创建一个字典，value为统计的出现频次，将出现频次最高的取出来放到一个list中，如果最高频次是1，则返回1
# 2. 遍历list中的值，在数组中从两边开始找，找到与list中元素相等最左和最右位置j,k，length=k-j+1
# 3. 返回最小的length即为最后的值




class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        maxfreq = []
        maxlengent = len(nums)
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = 1
            else:
                nums_dict[i] += 1
        freq = list(nums_dict.values())
        if max(freq) == 1:
            return 1
        for i in range(len(freq)):
            if freq[i] == max(freq):
                maxfreq.append(i)
        for j in range(len(maxfreq)):
            freqnum = list(nums_dict.keys())[maxfreq[j]]
            for num1 in range(len(nums)):
                if nums[num1] == freqnum:
                    a = num1
                    break
            for num2 in range(len(nums)-1,-1,-1):
                if nums[num2] == freqnum:
                    b = num2
                    break
            lengent = b-a+1
            maxlengent = min(maxlengent, lengent)
        return maxlengent
