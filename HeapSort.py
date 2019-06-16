import  random
class Heap:
    def __init__(self,A):
        self.A=A
        self.heapsize=len(A)

    def left(self,i):
        return 2*i

    def right(self,i):
        return 2*i-1

    def maxHeapify(self,i):
        l=self.left(i)
        r=self.right(i)
        if l<=self.heapsize and self.A[l-1]>self.A[i-1]:
            largest=l
        else:
            largest=i
        if r<=self.heapsize and self.A[r-1]>self.A[largest-1]:
            largest=r
        if largest!=i:
            self.A[i-1],self.A[largest-1]=self.A[largest-1],self.A[i-1]
            self.maxHeapify(largest)

    def buildMaxHeap(self):
        for i in range(self.heapsize//2,0,-1):
            self.maxHeapify(i)

    def heapSort(self):
        self.buildMaxHeap()
        for i in range(len(self.A),0,-1):
            self.A[0],self.A[i-1]=self.A[i-1],self.A[0]
            self.heapsize-=1
            self.maxHeapify(1)

if __name__=="__main__":
    # A=[16,14,10,8,7,9,3,1,4]
    # heap1=Heap(A)
    # heap1.heapSort()
    B = [random.randint(1, 100) for i in range(100)]
    print(B)
    heap1 = Heap(B)
    heap1.heapSort()
    print(B)

