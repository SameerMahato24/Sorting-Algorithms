# Code 1
def bubblesort(lst):
    l=len(lst)
    for i in range(l):
        isSwap=False
        for j in range(l-i-1):
            if(lst[j]>lst[j+1]):
                temp=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp
                isSwap=True

        if not isSwap:
            break        

    print(lst)
lst=[115,13,56,23,44,87,91,42]
bubblesort(lst)            


# Code 2
def bubblesort(lst):
    l = len(lst)
    for i in range(l-2,-1,-1):
        is_swap = False
        for j in range(0,i+1):
            if(lst[j] > lst[j+1]):
                lst[j],lst[j+1] = lst[j+1],lst[j]
                is_swap = True
        if(is_swap == False):
            break
    print(lst)
num=[115,13,56,23,44,87,91,42]
bubblesort(num) 
