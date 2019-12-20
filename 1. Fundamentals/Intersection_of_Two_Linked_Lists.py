#I know that an intersection occurs when a.nex= b.next
#Psuedocode approach:
#Traverse through A and store everything in a set
#Then go through B and see if at any point there is a node in set
#If there is, that means they intersect at the node in the set
#If we reach the end of the B traversal, then we know there was no intersection
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        pointerA= headA                     #O(1)
        nodeset=set()                       #O(1)
        while pointerA.next is not None:    #O(m)
            nodeset.add(pointerA)           #O(1)
            pointerA=pointerA.next          #O(1)
        nodeset.add(pointerA)               #O(1)
        pointerB=headB                      #O(1)
        while pointerB.next is not None:    #O(n)
            if pointerB in nodeset:         #O(1)
                return pointerB             #O(1)
            pointerB=pointerB.next          #O(1)
        if pointerB in nodeset:
            return pointerB
        else:
            return None                         #O(1)
    
        #Overall runtime = O(m)+O(n) = O(m+n) = linear runtime where m is size of A and n is size of B
        #Overall space complexity is O(n) since I am storing everything from A into a set
