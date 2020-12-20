#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   01_二叉树的最大深度.py
@Time    :   2020-11-23 13:54:54
@Author  :   ydongy
@Desc    :   https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnd69e/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self._depth(root)

    def _depth(self, node):
        if node is None:
            return 0
        return 1 + max(self._depth(node.left), self._depth(node.right))
