def bubble_sort(nums):
    i=0
    for i in range(0,len(nums)-i-1):
        for j in range(0,len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    print(nums)            
nums=[3,1,0,2,1,0]            
bubble_sort(nums)            