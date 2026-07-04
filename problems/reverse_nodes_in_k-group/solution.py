class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while True:
            node = prev
            for i in range(k):
                node = node.next
                if not node:
                    return dummy.next
            curr = prev.next
            nex = curr.next
            for i in range(k - 1):
                curr.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = curr.next
            prev = curr