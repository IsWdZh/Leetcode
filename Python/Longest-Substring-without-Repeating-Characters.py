# Given a string, find the length of the longest substring without repeating characters.
# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. 

# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


# My method:
# 从字符串最左侧开始，依次寻找，判断后一个是否在前面的子串中出现，如果有则记录最大长度...
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        n = len(s)
        if n<2:
            max_len = n
        for i in range(n-1):
            for j in range(i+1,n):
                if s[j] in s[i:j]:
                    if j-i>max_len:
                        right = j
                        left = i
                        max_len = right-left
                    break
                elif j == n-1:
                    if max_len<j-i+1:
                        max_len = j-i+1
        return max_len
        
