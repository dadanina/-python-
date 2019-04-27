#定义节点类
import numpy as np
class Node(object):
    def __init__(self,weight=None,name=None):
        self.weight=weight
        self.parent=-1
        self.lchild=-1
        self.rchild=-1
        self.name=name

maxbit=100
class Code(object):
    def __init__(self,maxbit,start=None):
        self.bit=[None for i in range(maxbit)]
        self.start=start

#定义huffmanTree
class huffmanTree(object):
    def __init__(self,alist):
        """
        alist: 给定字符和权重组成的列表
        """
        n=len(alist)
        #初始化节点(共2n-1个 其中前n个由输入给出)
        self.nodeList=[Node() for i in range(2*n-1)]
        for i in range(n):
            self.nodeList[i].name,self.nodeList[i].weight=alist[i][0],alist[i][1]

        #循环构造树
        #外层循环控制子树颗树2n-1-n=n-1
        #内层循环更新节点特征
        for i in range(n-1):
            m1=10000
            m2=10000
            x1=0
            x2=0
            for j in range(n+i):
                if self.nodeList[j].weight<m1 and self.nodeList[j].parent==-1:
                    m2=m1
                    x2=x1
                    m1=self.nodeList[j].weight
                    x1=j
                elif self.nodeList[j].weight<m2 and self.nodeList[j].parent==-1:
                    m2=self.nodeList[j].weight
                    x2=j
            self.nodeList[x1].parent=n+i
            self.nodeList[x2].parent=n+i
            self.nodeList[n+i].weight=m1+m2
            self.nodeList[n+i].lchild=x1
            self.nodeList[n+i].rchild=x2
            print("x1.weight and x2.weight in round",i+1,"  ",self.nodeList[x1].weight,"  ",self.nodeList[x2].weight)

    def Huffmancode(self,n):
        codeList=[Code(maxbit=maxbit) for i in range(30)]
        for i in range(n):
            cd=Code(maxbit=maxbit)
            cd.start=n-1
            c=i
            p=self.nodeList[i].parent
            while p!=-1:
                if self.nodeList[p].lchild==c:
                    cd.bit[cd.start]=0
                else:
                    cd.bit[cd.start]=1
                cd.start-=1
                c=p
                p=self.nodeList[c].parent
            codeList[i].bit=cd.bit
            codeList[i].start=cd.start
        return codeList

if __name__=="__main__":
    n=int(input("Please input n:"))
    alist=[]
    for i in range(n):
        l=[]
        l.append(input())
        l.append(float(input()))
        alist.append(l)
    print(alist)
    hufftree=huffmanTree(alist)
    codelist=hufftree.Huffmancode(n)
    for i in range(n):
        print(hufftree.nodeList[i].name,"huffman code is:",end=" ")
        for j in range(codelist[i].start+1,n):
            print(codelist[i].bit[j],end="")
        print(" ")
