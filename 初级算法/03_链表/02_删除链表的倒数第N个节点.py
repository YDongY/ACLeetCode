#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   02_删除链表的倒数第N个节点.py
@Time    :   2020-11-22 23:37:18
@Author  :   ydongy
@Desc    :   https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn2925/
"""

import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if fast is None:
            return slow.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return head

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        # 官方
        """
        n = 2
        dummy -> 1 -> 2 -> 3 -> 4 -> 5
        (second)　       (first)


        """
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
        self.head = ListNode(1)
        self.head.next = ListNode(2)
        self.head.next.next = ListNode(3)
        self.head.next.next.next = ListNode(4)
        self.head.next.next.next.next = ListNode(5)

    def test_success(self):
        self.s.removeNthFromEnd(self.head, 2)
        self._print()

    def _print(self):
        while self.head:
            print(self.head.val)
            self.head = self.head.next


if __name__ == '__main__':
    unittest.main()
