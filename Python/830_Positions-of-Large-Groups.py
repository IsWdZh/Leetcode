# In a string S of lowercase letters, these letters form consecutive groups of the same character.
# 
# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
# 
# Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.
# 
# The final answer should be in lexicographic order.
# 
#  
# 
# Example 1:
# Input: "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
# 
# Example 2:
# Input: "abc"
# Output: []
# Explanation: We have "a","b" and "c" but no large group.
# 
# Example 3:
# Input: "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]
#  
# 
# Note:  1 <= S.length <= 1000






# 在一个由小写字母构成的字符串 S 中，包含由一些连续的相同字符所构成的分组。
# 
# 例如，在字符串 S = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。
# 
# 我们称所有包含大于或等于三个连续字符的分组为较大分组。找到每一个较大分组的起始和终止位置。
# 
# 最终结果按照字典顺序输出。
# 
# 示例 1:
# 输入: "abbxxxxzzy"
# 输出: [[3,6]]
# 解释: "xxxx" 是一个起始于 3 且终止于 6 的较大分组。
# 
# 示例 2:
# 输入: "abc"
# 输出: []
# 解释: "a","b" 和 "c" 均不是符合要求的较大分组。
# 
# 示例 3:
# 输入: "abcdddeeeeaabbbcd"
# 输出: [[3,5],[6,9],[12,14]]
# 说明:  1 <= S.length <= 1000





# 解析：创建一个空的数组，然后从第二位开始遍历整个数组，将每个元素与前一个元素做比较，如果相等则count+1，如果出现该位元素与上一位不相等，
#       但是count大于等于3了，就将起始和结束元素的索引作为一个数组，加入空数组中；
#       如果遍历结束了，但是count的值不是1，大于3，说明最后几个元素都是相等的，所以将他们也作为一个数组加入大数组即可；


class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res = []
        count = 1
        for i in range(1, len(S)):
            if S[i] == S[i-1]:
                count += 1
            elif S[i] != S[i-1] and count >= 3:
                res.append([i-count, i-1])
                count = 1
            else:
                count = 1
        if count >= 3:
            res.append([len(S) - count, len(S)-1])
        return res
