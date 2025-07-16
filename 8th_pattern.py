n=int(input("enter the size"))

for row in range(5):
    for col in range(5):
        if row==0 or col==0 or row==n-1 or col==n-1:
            print("*",end='')
        else:
            print(' ',end='')
    print()
        
