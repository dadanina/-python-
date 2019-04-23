def fib(n):
    """
    计算斐波拉契数列的第n项
    """
    g=0
    f=1
    while n>0:
        g+=f
        f=g-f
        n-=1
    return g

if __name__=='__main__':
    print(fib(5))