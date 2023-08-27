def insertion_sort(nums):
    for i in range(1,len(nums)):
        for j in range(i,len(nums)):
            k=j
            while nums[k]<nums[k-1] and k>0:
                nums[k],nums[k-1]=nums[k-1],nums[k]
                k=k-1
    print(nums)        
nums=[3,1,2,2,1,0]            
insertion_sort(nums)     
