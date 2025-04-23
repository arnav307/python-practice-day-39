def fibonacci_series():
    a,b=0,1
    for i in range(1,6+1):
        print(a,end=" ")
        a,b=b,a+b
    return b
result=fibonacci_series()
print(result)