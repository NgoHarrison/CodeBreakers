def threeNumberSum(array, target):
    output = []
    array = sorted(array)
    #[-8, -6, 1, 2, 3, 5, 6, 12]
    for i in range(len(array)):
        left = i+1
        right = len(array) - 1
        while left < right:
            if array[i]+array[left]+array[right] == target:
                temp = sorted([array[i],array[left],array[right]])
                output.append(temp)
                left+=1
                right-=1
            elif array[i]+array[left]+array[right] < target:
                left+=1
            else:
                right-=1
    return output



array=[12,3,1,2,-6,5,-8,6]
#[[-8,2,6],[-8,3,5],[-6,1,5]]

print(threeNumberSum(array,0))
