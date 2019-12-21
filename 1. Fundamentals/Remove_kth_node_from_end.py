# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Pusdeocode:
# Initialize a variable to represent the size of the list
# Traverse through the array once and update the size
# Traverse through the array again but this time do it size-k
# Update pointers to represent removal
def removeKthNodeFromEnd(head, k):
    index = 0                           #O(1)
    temp = head                         #O(1)
    while temp.next is not None:        #O(k)
        temp = temp.next                #O(1)
        index += 1                      #O(1)
        temp2 = head                    #O(1)
    if k > index:                       #O(1)
        head.value = head.next.value    #O(1)
        head.next = head.next.next      #O(1)

    else:                               
        for i in range(index - k):      #O(k)
            temp2 = temp2.next          #O(1)

        temp2.next = temp2.next.next    #O(1)
        
#Overall runtime is O(k)+O(k) = O(k) = O(n) where k is the input length
#Overall space complexity is O(1)


 
