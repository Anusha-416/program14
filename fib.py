def fun(n):
    a=0
    b=1
    print(a)
    print(b)
    while a<n:
        c=a+b
        a=b
        b=c
        print(c)
fun(9)
