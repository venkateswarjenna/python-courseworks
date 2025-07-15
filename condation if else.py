items=['coffee','icecream','samosa','idly']
stocks=[20,50,40,0]
data=input("enter the item: ")

if data in items:
    ind=items.index(data)
    if stocks[ind]>0:
        print("AvA")
    else:
        print('out of stock".plese try again')
        

else:
    print('Iteams not ava')
