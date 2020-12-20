#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   05_验证回文串.py
@Time    :   2020-11-23 14:03:58
@Author  :   ydongy
@Desc    :   https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xne8id/
"""

import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        原字符串 + 双指针
        :param s:
        :return:
        """
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
        return True

    def isPalindrome2(self, s: str) -> bool:
        """
        1. 保留字母和数字字符，去除其他字符，得到新字符
        2.
            - 2.1 : 对新字符反转与新字符比较
            - 2.2 : 双指针判断新字符
        :param s:
        :return:
        """
        pass


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_success(self):
        self.assertEqual(self.s.isPalindrome("A man, a plan, a canal: Panama"), True)
        self.assertEqual(self.s.isPalindrome("race a car"), False)


if __name__ == '__main__':
    unittest.main()
