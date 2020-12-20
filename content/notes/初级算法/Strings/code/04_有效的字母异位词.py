#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   04_有效的字母异位词.py
@Time    :   2020-11-23 13:57:36
@Author  :   ydongy
@Desc    :   https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn96us/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = [0] * 26
        l2 = [0] * 26

        for i in s:
            l1[ord(i) - 97] += 1

        for j in t:
            l2[ord(j) - 97] += 1

        return l1 == l2

    def isAnagram2(self, s: str, t: str) -> bool:
        l1 = list(s)
        l2 = list(t)

        l1.sort()
        l2.sort()

        return l1 == l2
