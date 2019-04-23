def maxCount(a,ma):
    a.sort()
    ans=0
    tw=0.0
    while tw<=ma:
        tw+=a.pop(1)
        ans+=1
    return ans-1

if __name__=="__main__":
    print("请输入古董重量：")
    w=list(map(float,input().split()))
    mw=int(input("请输入最大载重量: "))
    ans=maxCount(w,mw)
    print("能装入古董的最大数量是:",ans)
