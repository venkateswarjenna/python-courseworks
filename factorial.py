def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*1
    return fact




n=int(input("enter the number: "))
for i in range(1,n+1):
    print(f"{i}!={factorial(i)}")
    
