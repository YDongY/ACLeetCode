#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   04_存在重复元素.py
@Time    :   2020-11-22 22:36:36
@Author  :   ydongy
@Desc    :   https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x248f5/
"""

from typing import List
import unittest


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _map = {}

        for num in nums:
            if num not in _map:
                _map[num] = True
            else:
                return True
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_success(self):
        self.assertEqual(self.s.containsDuplicate(nums=[1, 2, 3, 1]), True)
        self.assertEqual(self.s.containsDuplicate(nums=[1, 2, 3, 4]), False)
        self.assertEqual(self.s.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)

        self.assertEqual(self.s.containsDuplicate2(nums=[1, 2, 3, 1]), True)
        self.assertEqual(self.s.containsDuplicate2(nums=[1, 2, 3, 4]), False)
        self.assertEqual(self.s.containsDuplicate2(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)


if __name__ == '__main__':
    unittest.main()
