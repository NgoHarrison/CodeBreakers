def binary(array,target):
    lo = 0 
    hi = len(array)-1
        
    while lo <= hi:
        mid = (lo+hi)//2
        if array[mid] == target:
            return True
        else:
            if array[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        print(lo,hi)
    return False

def searchMatrix(matrix,target):
    lo = 0
    hi = len(matrix)-1
    if len(matrix) == 1:
        return binary(matrix[0],target)
    while lo <= hi:
        print(lo,hi)
        mid = (lo+hi)//2
        if matrix[mid][0] <= target and matrix[mid][len(matrix[mid])-1] >= target:
            return binary(matrix[mid], target)
        elif matrix[mid][0] > target:
            hi = mid - 1
        elif matrix[mid][0] == target:
            return True
        elif matrix[mid][0] < target and matrix[mid][len(matrix[mid])-1] < target:
            lo = mid + 1

#print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],7))
