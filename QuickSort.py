import random
def quickSort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)

def partition(A,p,r):
    ro=random.randint(p,r)
    A[ro],A[r]=A[r],A[ro]
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

if __name__=="__main__":
    A=[10,5,3,1,7,2,8]
    quickSort(A,0,len(A)-1)
    print(A)

