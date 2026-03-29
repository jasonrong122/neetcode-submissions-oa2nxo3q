# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        stack = []
        while curr:
            stack.append(str(curr.val))
            curr = curr.next
        
        arr = []
        while stack:
            arr.append(stack.pop())

        res = "".join(arr)


        curr2 = l2
        stack2 = []
        while curr2:
            stack2.append(str(curr2.val))
            curr2 = curr2.next
        
        arr2 = []
        while stack2:
            arr2.append(stack2.pop())

        res2 = "".join(arr2)

        total = str(int(res) + int(res2))

        newStack = []
        for i in range(len(total)):
            newStack.append(total[i])

        dummy = ListNode()
        currHead = dummy

        while newStack:
            val = newStack.pop()
            currHead.next = ListNode(int(val))
            currHead = currHead.next
        
        return dummy.next