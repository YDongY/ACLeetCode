#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   05_回文链表.py
@Time    :   2020-11-23 13:14:00
@Author  :   ydongy
@Desc    :   https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnv1oc/
"""
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # 查找中间节点,如果是偶数得到前一个
        mid_node = self.middle_node(head)

        # 反转后半部分链表
        new_head = self.reverse(mid_node.next)  # 从中间结点下一个开始

        while new_head:
            if head.val == new_head.val:
                head = head.next
                new_head = new_head.next
            else:
                return False
        # 还原链表并返回结果
        mid_node.next = self.reverse(new_head)
        return True

    def middle_node(self, node):
        slow = fast = node

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self, mid_node):
        prev, cur = None, mid_node

        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
        self.head = ListNode(1)
        self.head.next = ListNode(1)
        self.head.next.next = ListNode(2)
        self.head.next.next.next = ListNode(1)

    def test_success(self):
        cur = self.head
        p = self.s.isPalindrome(cur)
        while p:
            print(p.val)
            p = p.next


if __name__ == '__main__':
    unittest.main()
