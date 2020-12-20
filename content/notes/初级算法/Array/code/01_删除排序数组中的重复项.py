#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   01_删除排序数组中的重复项.py
@Time    :   2020-11-22 21:39:12
@Author  :   ydongy
@Desc    :   https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2gy9m/
"""
from typing import List
import unittest


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        point1 = 0
        point2 = 1
        while point2 < len(nums):
            if nums[point2] != nums[point1]:
                point1 += 1
                nums[point1] = nums[point2]
            point2 += 1
        print(nums)
        return point1 + 1

    def removeDuplicates2(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        point = 0

        for i in range(1, len(nums)):  # 利用 i 替换 point2
            if nums[i] != nums[point]:
                point += 1
                nums[point] = nums[i]
        return point + 1


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_success(self):
        self.assertEqual(self.s.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)
        self.assertEqual(self.s.removeDuplicates(nums=[1, 1, 2]), 2)
        self.assertEqual(self.s.removeDuplicates(nums=[1]), 1)
        self.assertEqual(self.s.removeDuplicates(nums=[]), 0)
        self.assertEqual(self.s.removeDuplicates2(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)
        self.assertEqual(self.s.removeDuplicates2(nums=[1, 1, 2]), 2)
        self.assertEqual(self.s.removeDuplicates2(nums=[1]), 1)
        self.assertEqual(self.s.removeDuplicates2(nums=[]), 0)


if __name__ == '__main__':
    unittest.main()
