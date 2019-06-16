def mergeSort(arr,l,r):
    if l==r:return
    else:
        mid=l+(r-l)//2
        mergeSort(arr,l,mid)
        mergeSort(arr,mid+1,r)
        merge(arr,l,mid+1,r)

def merge(arr,leftPtr,rightPtr,rightbound):
    k=[]
    i=leftPtr
    j=rightPtr
    while i<=rightPtr-1 and j<=rightbound:
        if(arr[i]<=arr[j]):
            k.append(arr[i])
            i+=1
        else:
            k.append(arr[j])
            j+=1
    while i<=rightPtr-1:
        k.append(arr[i])
        i+=1
    while j<=rightbound:
        k.append(arr[j])
        j+=1
    for i in range(len(k)):
        arr[leftPtr+i]=k[i]

if __name__=="__main__":
    arr=[1,5,2,4,7,1,3]
    mergeSort(arr,0,len(arr)-1)
    print(arr)