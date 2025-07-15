bullets=10
while bullets>0:
    if bullets == 5:
        print("deed")
        break
    print(f"{bullets} are left-you can shoot()")
    bullets-=1
else:
    print("game over")
