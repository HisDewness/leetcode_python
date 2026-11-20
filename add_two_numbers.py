# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order,and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # Given two linked lists of non-negative ints, digits in reverse order
        # Actual passed in values are the heads of each list

        # Lists to fill with the contents of the linked lists
        list1 = []
        list2 = []

        final_answer = []

        # Get values of lists in order - iterate from head to tail
        while l1 is not None:
            list1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            list2.append(l2.val)
            l2 = l2.next

        # No reverse needed: index 0 is already the ones digit,
        # which is where addition starts

        # Iterate and add each element, carrying overflow into the next position
        carry = 0
        for i in range(max(len(list1), len(list2))):
            # If one list ran out of digits, treat its digit as 0
            digit1 = list1[i] if i < len(list1) else 0
            digit2 = list2[i] if i < len(list2) else 0
            total = digit1 + digit2 + carry

            # If the addition is less than 10, store the number outright
            if total < 10:
                final_answer.append(total)
                carry = 0
            # If not, store the ones digit and carry 1 to the next position
            else:
                final_answer.append(total - 10)
                carry = 1

        # Leftover carry becomes a new highest digit (e.g. 5 + 5 = 10 -> [0, 1])
        if carry:
            final_answer.append(carry)

        # Turn final_answer into a linked list
        # final_return stays on the head, current moves forward attaching nodes
        final_return = ListNode(final_answer[0])
        current = final_return
        for j in range(1, len(final_answer)):
            current.next = ListNode(final_answer[j])
            current = current.next

        return final_return