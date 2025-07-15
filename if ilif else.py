items=['coffee','icecream','samosa','idly']
stocks=[20,50,40,0]
distance=[13,4,9,12]
rating=[3.2,4,4.3,1]
cost=[150,60,20,40]
veg=[True,True,False,True]
time=[40,30,25,15]

data=input("enter the item: ")
ind=items.index(data)
if distance[ind]<5 and rating[ind]>4 and cost[ind]<500 and veg[ind] and time[ind]<30:
    print('fil appl')
elif distance[ind]<5 and rating[ind]>4 and cost[ind]<500 and veg[ind]:
    print('Time not matters')
elif distance[ind]<5 and rating[ind]>4 and cost[ind]<500:
    print('Veg status not requried')
elif distance[ind]<5 and rating[ind]>4:
    print('distanc and rating applied')
elif rating[ind]>4:
    print('rating applied')
elif distance[ind]<5:
    print('distance applied')
elif cost[ind]<500:
    print( 'cost applied')
else:
     print('thankyou:')
        
        
