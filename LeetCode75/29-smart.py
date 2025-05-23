class Solution(object):
    def deleteMiddle(self, head):
        if head == None:
            return None
        prev = ListNode(0)
        prev.next = head
        slow = prev
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next        
        slow.next = slow.next.next
        return prev.next