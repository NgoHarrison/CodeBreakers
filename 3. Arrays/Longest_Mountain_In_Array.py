
def longestMountain(A):
    print(A)
    left = 0
    right = len(A)-1
    while left < right:
        
        #print(A[left:right+1])
        middle = (right+left)//2
        print(left,middle,right)
        temp = sorted(A[left:middle+1])+sorted(A[middle+1:right+1],reverse=True)
        if len(temp) < 3:
            return 0
        if temp == A[left:middle]+A[middle:right+1] and len(temp)==(len(set(temp[0:middle]))+len(set(temp[middle:len(temp)]))):
            if temp[len(temp)//2] > temp[(len(temp)//2)-1] and temp[len(temp)//2] > temp[(len(temp)//2)+1]:
                return right-left+1
        if A[left+1] <= A[left] and A[right] < A[right-1]:
            left+=1
        elif A[left+1] > A[left] and A[right] >= A[right-1]:
            right-=1
        else:
            left+=1
            right-=1
    return 0



arr=[0,1,2,3,4,5,4,3,2,1,0]
arr2=[2,2,2]
arr3=[2,1,4,7,3,2,5]
arr4=[0,1,2,3,4,5,6,7,8,9,10,8,7,6,5,4,3,2,1,0]
arr5=[0,1,2,3,4,5,6,7,8,9]
arr6=[0,1,0,2,2]
arr7=[4,2,9,8,0]
print(longestMountain(arr7))
#print(arr[0:2]+arr[2:4])
#print('-------')
#middle = 3
#print(sorted(arr[0:middle]+arr[middle:len(arr)]))
#temp = sorted(arr,reverse=True)

#print(arr)
#print(temp)
#print(arr==temp[0:len(temp)])
