#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   06_环形链表.py
@Time    :   2020-11-23 13:49:39
@Author  :   ydongy
@Desc    :   https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnwzei/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
