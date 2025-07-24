def shoot(n):
    if n==1:
        return 1
    print("Before recusion: ",n)
    shoot(n-1)
    print("After recusion: ",n)

shoot(10)

n=int(input("enete the valaue: "))
shoot(n)
