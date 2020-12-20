#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   03_反转链表.py
@Time    :   2020-11-23 12:39:30
@Author  :   ydongy
@Desc    :   https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnnhm6/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

    def reverseList2(self, head: ListNode) -> ListNode:
        """
        递归
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        newHead = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return newHead
