n = int(input("Enter the no. for which you want Fibonacci Series value : "))
def Fibonacci(n):
    fib_List = [1,1]
    for i in range(2,n):
        if i >=2:
           fib_List.append(fib_List[i-1]+ fib_List[i-2])
    return fib_List

result = Fibonacci(n)
if n ==1:
    print(result[0])
elif n==2:
    print(result[1])
else:
    print(result[n-1])
            
        

