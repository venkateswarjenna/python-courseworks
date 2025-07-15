l=['smart phones','laptops','airpods','shoes']
for i in l:
    if i=="airpods":
     break
    print(i.center(20,'_'))
else:
    print("end of the items")


    
        
bullets=10
while bullets>0:
    if bullets ==5:
        print("ded")
        break
    print("shoot()")
    bullets-=1
else:
     print("game over")
