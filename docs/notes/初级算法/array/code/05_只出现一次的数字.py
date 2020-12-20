#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   05_只出现一次的数字.py
@Time    :   2020-11-22 22:44:04
@Author  :   ydongy
@Desc    :   https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x21ib6/
"""

from typing import List
import unittest

from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        _map = {}

        for num in nums:
            if num not in _map:
                _map[num] = 1
            else:
                _map[num] += 1

        for k, v in _map.items():
            if v == 1:
                return k

    def singleNumber2(self, nums: List[int]) -> int:
        # 位运算：异或
        return reduce(lambda x, y: x ^ y, nums)


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_success(self):
        self.assertEqual(self.s.singleNumber(nums=[2, 2, 1]), 1)
        self.assertEqual(self.s.singleNumber(nums=[4, 1, 2, 1, 2]), 4)

        self.assertEqual(self.s.singleNumber2(nums=[2, 2, 1]), 1)
        self.assertEqual(self.s.singleNumber2(nums=[4, 1, 2, 1, 2]), 4)


if __name__ == '__main__':
    unittest.main()
