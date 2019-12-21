#Psuedocode
#Initialize a list but use it as a stack structure
#Everytime an operation is read, pop the last two elements and complete operation
#Push result back onto "stack"
#Keep doing this until all tokens are processed



def isOperator(token):
    if token =='+' or token =='-' or token =='*' or token =='/':
        return True
    return False
    
def op(left,right,token):
    left = int(left)
    right = int(right)
    if token=='+':
        return left+right
    elif token=='-':
        return left-right
    elif token=='*':
        return left*right
    else:
        return int(left/right)

class Solution:
           
    def evalRPN(self, tokens: List[str]) -> int:
        lst = []                                        #O(n)
        for i in tokens:                                #O(n)
            if not isOperator(i):                       #O(1)
                lst.append(i)                           #O(1)
            else:                                       #O(1)
                right = lst.pop()                       #O(1)
                left = lst.pop()                        #O(1)
                lst.append(op(left,right,i))            #O(1)
        return lst[0]                                   #O(1)

#Overall time complexity is O(n)
#Overall space complexity is O(n) since I am using a stack to keep track of tokens processed
    
    
    
