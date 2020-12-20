#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   03_字符串中的第一个唯一字符.py
@Time    :   2020-11-22 23:12:40
@Author  :   ydongy
@Desc    :   
"""
import unittest


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        _map = {}
        for i, v in enumerate(s):
            if s[i] not in _map:
                _map[v] = i
            else:
                _map[v] = -1

        for k, v in _map.items():
            if v != -1:
                return v
        return -1


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_success(self):
        self.assertEqual(self.s.firstUniqChar("leetcode"), 0)
        self.assertEqual(self.s.firstUniqChar("loveleetcode"), 2)
        self.assertEqual(self.s.firstUniqChar("llee"), -1)
        self.assertEqual(self.s.firstUniqChar(""), -1)


if __name__ == '__main__':
    unittest.main()
