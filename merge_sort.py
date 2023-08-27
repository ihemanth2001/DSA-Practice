def merge_sort(nums):
    if len(nums)>1:
        mid=len(nums)//2
        L=nums[:mid]
        R=nums[mid:]
        merge_sort(L)
        merge_sort(R)
        k=0
        i=0
        j=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                nums[k]=L[i]
                i=i+1
                k=k+1
            else:
                nums[k]=R[j]
                j=j+1
                k=k+1
      
        while(i<len(L)):
            nums[k]=L[i]
            k=k+1
            i=i+1
        while(j<len(R)):
            nums[k]=R[j]
            j=j+1
            k=k+1
nums=[3,1,2,2,1,0]            
merge_sort(nums)     
print(nums)