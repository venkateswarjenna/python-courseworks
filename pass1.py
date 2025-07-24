def update(n):
    print("Before-  inside of the function:",n)
    n.add(5)
    print("After-  inside of the function:",n)

n={1:1,2:4,3:9,4:16,5:25}
update(n)
print("outside of the function:",n)
    
