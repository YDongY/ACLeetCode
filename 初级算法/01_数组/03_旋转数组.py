#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   03_旋转数组.py
@Time    :   2020-11-22 22:01:36
@Author  :   ydongy
@Desc    :   https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2skh7/
"""

import unittest
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 暴力
        for _ in range(k):
            for j in range(1, len(nums)):
                nums[0], nums[j] = nums[j], nums[0]

        return nums

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Eg:
           [1,2,3,4,5,6,7]
        -> [7,6,5,4,3,2,1]
             /      \
        -> [7,6,5] [4,3,2,1]
              /        \
        -> [5,6,7] [1,2,3,4]
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

        return nums

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_success(self):
        self.assertEqual(self.s.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3), [5, 6, 7, 1, 2, 3, 4])
        self.assertEqual(self.s.rotate(nums=[-1, -100, 3, 99], k=2), [3, 99, -1, -100])


if __name__ == '__main__':
    unittest.main()
