#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   01_反转字符串.py
@Time    :   2020-11-22 22:54:06
@Author  :   ydongy
@Desc    :   https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnhbqj/
"""

from typing import List
import unittest


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return s


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_success(self):
        self.assertEqual(self.s.reverseString(["h", "e", "l", "l", "o"]), ["o", "l", "l", "e", "h"])
        self.assertEqual(self.s.reverseString(["H", "a", "n", "n", "a", "h"]), ["h", "a", "n", "n", "a", "H"])


if __name__ == '__main__':
    unittest.main()
