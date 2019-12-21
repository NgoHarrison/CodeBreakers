# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#Psuedocode:
#Store values in list
#Use two pointers and position one at front and one at end
#If two pointers do not equal in value, then this isn't a palindrome
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lst = []                                #O(1)
        temp = head                             #O(1)
        while temp is not None:                 #O(n)
            lst.append(temp.val)                #O(1)
            temp = temp.next                    #O(1)
        front = 0                               #O(1)
        back = len(lst)-1                       #O(1)
        while back > front:                     #O(n)
            if lst[front]!=lst[back]:           #O(1)
                return False                    #O(1)
            front+=1                            #O(1)
            back-=1                             #O(1)
        return True                             #O(1)

#Overall time complexity is O(n) + O(n) = O(n) where n is the number of nodes in list
#Overall space complexity is O(n) since I am storing the node values in a list 
