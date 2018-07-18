# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always exist in the array.
# 
# Example 1:
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# Input: [2,2,1,1,1,2,2]
# Output: 2


# 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 
# 你可以假设数组是非空的，并且给定的数组总是存在众数。
# 
# 示例 1:
# 输入: [3,2,3]
# 输出: 3
# 
# 示例 2:
# 输入: [2,2,1,1,1,2,2]
# 输出: 2

# 解析：（该方法有点儿慢) 先将nums 转为集合去重，然后检查存在的这些元素分别重复的次数，只要重复次数大于n/2，则返回该值

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = list(set(nums))
        n = len(nums)
        m = len(s)
        for i in range(m):
            count = 0
            for j in range(n):
                if s[i] == nums[j]:
                    count += 1
            if count > n/2:
                return s[i]
