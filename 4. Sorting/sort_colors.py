
def sortColors(nums):
    start=0
    finish = len(nums)-1
    p=0
    while p < finish:
        if nums[p] == 0:
            nums[p],nums[start]=nums[start],nums[p]
            start+=1
            p+=1
        elif nums[p]==2:
            nums[p],nums[finish]=nums[finish],nums[p]
            finish-=1
            p+=1
        else:
            p+=1
    



    
lst = [2,0,2,1,1,0]
print(lst)
sortColors(lst)
print(lst)
