def insertionsort(lst):
    l=len(lst)
    for i in range(1,l):
        key=lst[i]
        j=i-1
        while(j>=0 and lst[j]>key):
            lst[j+1]=lst[j]
            j=j-1
        lst[j+1]=key
    print(lst) 
lst=[11,45,7,2,9,34,67,99,32,56,79,14,78,57]
insertionsort(lst)
