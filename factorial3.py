'''n=int(input("enter the num: "))
sum=0
for i in n:
    sum+=int(i)
print(sum)'''


'''
n=int(input("enter the num: "))
def sumofdigits(n):
    if n ==0:
        return 0
    return n% 10 + sumofdigits(n//10)
print(sumofdigits(n))
'''

'''
n=int(input("enter the num: "))
a=0
b=1
if n==1:
    print(a)
elif n==2:
    print(b)
elif n>2:
    print(a)
    print(b)
    for i in range(n-2):
        c = a+b
        print(c)
        a=b
        b=c
,,,


