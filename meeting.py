if __name__=="__main__":
    n=int(input("请输入会议总数："))
    a=[]
    for i in range(n):
        b=list(map(int,input().split()))
        b.insert(0,i+1)
        a.append(b)
    a.sort(key=lambda x:x[2])
    count=1
    last=a[0][-1]
    print("选择的会议过程：")
    print("选择第"+str(a[0][0])+"个会议")
    for i in range(1,n):
         if a[i][1]>=last:
            count+=1
            last=a[i][-1]
            print("选择第"+str(a[i][0])+"个会议")
    print("最多可安排"+str(count)+"个会议")