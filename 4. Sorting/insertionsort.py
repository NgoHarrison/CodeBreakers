
def insertionSortList(self, head: ListNode) -> ListNode:
    if not head:
        return None
    arr=[]
        
    cur = head
    while cur:
        arr.append(cur.val)
        cur = cur.next
    for i in range (1,len(arr)):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
            else:
                break
    temp = ListNode(arr[0])
    cur = temp
    for i in range(1,len(arr)):
        temp2 = ListNode(arr[i])
        cur.next = temp2 
        cur = temp2
    return temp
