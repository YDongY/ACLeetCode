#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   02_整数反转.py
@Time    :   2020-11-22 22:58:32
@Author  :   ydongy
@Desc    :   https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnx13t/
"""

import unittest


class Solution:
    def reverse(self, x: int) -> int:
        tag = False
        if x < 0:
            x = abs(x)
            tag = True
        res = 0
        while x != 0:
            if res > ((2 << 30) - 1 - x % 10) / 10 or x < (-1 * (2 << 30) - x % 10) / 10:
                return 0
            res = res * 10 + x % 10
            x = x // 10
        if tag:
            res *= -1
        return res


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_success(self):
        self.assertEqual(self.s.reverse(123), 321)
        self.assertEqual(self.s.reverse(-123), -321)
        self.assertEqual(self.s.reverse(120), 21)


if __name__ == '__main__':
    unittest.main()
