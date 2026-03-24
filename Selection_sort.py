# def selectionsort(nums):
#     n=len(nums)
#     for i in range(n):
#         min=nums[i]
#         index=i
#         for j in range(i+1,n):
#             if(nums[j]<min):
#                 min=nums[j]
#                 index=j
#         temp=nums[i]
#         nums[i]=nums[index]
#         nums[index]=temp
#     print(lst)

# lst=[5,1,1,2,0,0,15,22,11,50,23,67,34]
# selectionsort(lst)   

def selectionsort(nums):
    l = len(nums)
    for i in range(l):
        min_index = i
        for j in range(i+1,l):
            if (nums[j] < nums[min_index]):
                min_index = j
        nums[i],nums[min_index] = nums[min_index],nums[i]
    print(nums)
lst=[5,1,1,2,0,0,15,22,11,50,23,67,34]
selectionsort(lst) 