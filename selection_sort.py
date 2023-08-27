def selection_sort(nums):
    i=0
    k=999999
    for i in range(len(nums)):
        smallest=nums[i]
        for j in range(i,len(nums)):
            if nums[j]<smallest:
                k=j
                smallest=nums[j]
        nums[i],nums[k]=nums[k],nums[i]    
        print(nums)
nums=[3,1,0,2,1,0]            
selection_sort(nums)            