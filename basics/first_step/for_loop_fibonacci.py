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

"""While creating a function you need to return list here and also create a object from 
 from outside function. In the question given use the simple formula for fibonacci ,also for a
 new index we cannot directly insert value like l[i] = l[i-1], you need to use apppend or other
 list function as per
 """   
            
        

