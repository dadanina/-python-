if __name__=="__main__":
    n=int(input("请输入宝物的数量："))
    tw=float(input("请输入驴子的载重量："))
    a=[]
    for i in range(n):
        b=list(map(float,input().split()))
        b.append(b[1]/b[0])
        a.append(b)
    val=0
    a.sort(key=lambda x:x[2])
    a.reverse()
    for i in range(n):
        if a[i][0]<tw:
            val+=a[i][1]
            tw-=a[i][0]
        else:
            val+=a[i][2]*tw
            break
    print("装入宝物的最大价值是：",val)