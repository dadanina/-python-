import math
def prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1

#method 1: 998*(3+5+7+...+1999)*sqrt(i)
if __name__=="__main__":
    for i in range(4,2000,2):
        for j in range(1,i):
            if prime(j):
                if prime(i-j):
                    print(j,i-j)
                    break
        if j==i:
            print('error')
            break

#method 2:
if __name__=="__main__":
    #记录分解得到的数[2,1998]是不是素数
    flag=[1]
    for i in range(2,1998):
        flag.append(prime(i))
    for i in range(4,2000,2):
        for j in range(1,i):
            if flag[j-1]:
                if flag[i-j-1]:
                    print(j,i-j)
                    break
        if j==i:
            print('error')
            break

#method 3:
if __name__=="__main__":
    data=[1]
    for i in range(2,1998):
        if prime(i):
            data.append(i)
    for i in range(4,2000,2):
        for j in range(1,i):
            if j in data:
                if i-j in data:
                    print(j,i-j)
                    break
        if j==i:
            print('error')
            break

# method 4 最慢
if __name__=="__main__":
    data=[1]
    for i in range(2,1998):
        if prime(i):
            data.append(i)
    for i in range(4,2000,2):
        for j in range(len(data)):
            for m in range(j+1,len(data)):
                if data[j]+data[m]==i:
                    print(data[j],data[m])
                    break
        if j==len(data):
            print('error')
            break


