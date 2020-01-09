def help(node):
    t = node
    while t:
        print(t.val)
        t=t.next
    print('-----------')

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

def insertionSortList(head):
    if not head:
        return None
    elif head.next==None:
        return head
    else:
        begin = ListNode('dummy')
        begin.next = head
        cur = begin.next.next
        help(head)
        print('BEGIN')
        while cur:
            cur2 = begin.next
            print(cur.val,cur2.val)
            while cur2:
                if cur2.val > cur.val:
                    temp = cur.next
                    begin.next = cur
                    cur.next = cur2
                    cur2.next = temp
                    print('---------DUMMY------------')
                    help(begin)
                    print('--------END DUMMY--------')
                    break
                
                else:
                    cur2=cur2.next
            help(begin.next)
            cur=cur.next
        return begin.next

a = ListNode(4)
b = ListNode(2)
c = ListNode(1)
d = ListNode(3)
a.next = b
b.next = c
c.next = d

insertionSortList(a)







            
