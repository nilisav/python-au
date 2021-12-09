# Linked List

+ [Merge Two Sorted Lists](#merge-two-sorted-lists)

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
from solution import Solution2
from solution import ListNode2
class TestMergeTwoLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def get_linked_list_values(self, head):
        result = []
        cur = head
        while cur is not None:
            result.append(cur.val)
            cur = cur.next
        return result
    def create_linked_list(self, values):
        values.reverse()
        if not values:
            return None
        prev_node = ListNode(values[0])
        for i in range(1, len(values)):
            next_node = ListNode(values[i], prev_node)
            prev_node = next_node
        return prev_node
    def test_merge(self):
        list1 = self.create_linked_list([1, 2, 4, 7, 8])
        list2 = self.create_linked_list([1, 5, 8])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.get_linked_list_values(result), [1, 1, 2, 4, 5, 7, 8, 8])
    def test_empty_list(self):
        self.assertEqual(self.get_linked_list_values(self.solution.mergeTwoLists(None, None)), [])
    def test_one_value(self):
        list1 = self.create_linked_list([1])
        list2 = self.create_linked_list([])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.get_linked_list_values(result), [1])

if __name__ == "__main__":
    unittest.main()
```

</blockquote></details>




``` python
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = None
        if list1 and list2:
            if list1.val < list2.val:
                head = res = list1
                list1 = list1.next
            else:
                head = res = list2
                list2 = list2.next
        else:
            if list1:
                head = res = list1
            if list2:
                head = res = list2
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        while list1:
            head.next = list1
            head = head.next
            list1 = list1.next
        while list2:
            head.next = list2
            head = head.next
            list2 = list2.next
        return res
```