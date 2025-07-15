currect_username="Venky"
currect_password="1234"
attempts=3

while attempts>0:
    username=input("enter username")
    password=input("enter password")
    if username== currect_username and password== currect_password:
        print("login succes")
        break
    else:
        attempts -=1
        print(f"invalide id and password,pls try again.{attempts}:")
else:
    print("you hame limit your time out pls try again after 24 hrs")