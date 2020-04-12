"""
大致思路是使用滑动窗口来解决，使用 hash_map 优化查找，进一步优化可以使用数组
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        start, end = 0, 1

        hash_map = {s[start]: start}
        max_length = 1

        while start < end and end < len(s):
            if s[end] in s[start: end]:
                start = hash_map[s[end]] + 1
                hash_map[s[end]] = end
                end += 1
            else:
                hash_map[s[end]] = end
                end += 1
                max_length = max(max_length, end - start)

        return max_length
