# Code 1
def merge(nums,l,mid,r):
    a=[]
    b=[]
    for i in range(l,mid+1):
        a.append(nums[i])
    for i in range(mid+1,r+1):
        b.append(nums[i])

    i,j,k=0,0,l
    
    while(k<=r):
        if(j==len(b)):
            nums[k]=a[i]
            i+=1
            k+=1
        elif(i==len(a)):
            nums[k]=b[j]
            j+=1
            k+=1
        elif(a[i]<b[j]):
            nums[k]=a[i]
            i+=1
            k+=1
        else:
            nums[k]=b[j]
            j+=1
            k+=1

# Code 2
def mergeSort(nums,l,r):
    if(l>=r):
        return

    mid=(l+r)//2
    mergeSort(nums,l,mid)
    mergeSort(nums,mid+1,r)
    merge(nums,l,mid,r)

def sortArray(nums):
    mergeSort(nums,0,len(nums)-1)
    return nums 

nums=[11,45,7,2,9,34,67,99,32,56,79,14,78,57]
print(sortArray(nums))                               
