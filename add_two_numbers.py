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
        # Given two linked lists with positive ints, stored descending
        # Actual passed in values are the heads of each list

        # ListNodes saving the head of each passed in list (l1 and l2)
        head1 = l1
        head2 = l2

        # Lists to fill with the contents of the linked lists
        list1 = []
        list2 = []

        final_answer = []

        # Get values of lists in order - iterate from head to tail
        while l1 != None:
            list1.append(list1.val)
        while l2 != None:
            list2.append(list2.val)

        # Get the order right for traditional addition
        list1.reverse
        list2.reverse

        # Iterate and add each element, with overflow setting the next
        # position as 1 in the final list
        for i in range(len(list1)):
            # If the addition is less than 10, store the number outright
            if(list1[i] + list2[i]) < 10:
                final_answer[i] = list1[i] + list2[i]
                # If not, get the overflow above 10 to the next position
            else:
                final_answer[i] = ((list1[i] + list2[i]) - 10)
                final_answer[i+1] = (list1[i] + list2[i]) - final_answer[i]
        
        # Once iteration is done and final_answer is filled, parse 
        # and turn into combination of ListNode elements where self.val
        # is the int value itself
        final_return = ListNode(final_answer[0]) 
        for j in range(len(final_answer)):
            final_return.next = ListNode(final_answer[j], None)
        
        return final_return