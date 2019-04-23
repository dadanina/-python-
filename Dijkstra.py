import numpy as np
def dijkstra(M,N,flag,dist,p,u):
    #设置源点进入S
    flag[u] = True
    dist[u] =0
    while False in flag:
        temp=1e7
        t=u
        for i in range(N):
            if (not flag[i]) and dist[i]<temp:
                temp=dist[i]
                t=i
        # if t==u:
        #     return
        flag[t]=True
        for j in range(N):
            if (not flag[j]) and M[t][j]<1e7:
                if dist[j]>dist[t]+M[t][j]:
                    dist[j]=dist[t]+M[t][j]
                    p[j]=t

def findpath(u,dist,p):
    print("源点为：",u)
    s=[]
    for i in range(N):
        x=p[i]
        while x!=-1:
            s.append(x)
            x=p[x]
        print("源点到其他各顶点最短路径是：")
        while len(s):
            print(str(s[-1]+1)+"---",end="")
            s.pop()
        print(str(i+1),"最短距离为：",dist[i])

if __name__=="__main__":
    N=int(input("请输入城市的个数："))
    L=int(input("请输入城市之间路线的个数："))
    I=[]
    for i in range(L):
        I.append(list(map(int,input().split())))
    M=np.ones(shape=(N,N))*1e7
    for m,n,i in I:
        M[m-1][n-1]=i
    u=int(input("请输入小明所在的位置："))
    flag = [False for i in range(N)]
    dist = [M[u-1][i] for i in range(N)]
    p = [-1 if dist[i] == 1e7 else u-1 for i in range(N)]
    dijkstra(M, N, flag, dist, p, u-1)
    print(dist)
    print(p)
    findpath(u,dist,p)
