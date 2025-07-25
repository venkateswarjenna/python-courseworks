data={"Balance": 150000, "History":[]}

def current_balance():
    print(f"{data['Balance']}")

def deposit():
    amount=int(input("Enter the amount: "))
    data['Balance']+=amount
    data['History'].append(f"deposited-{amount}")
    print(f"deposited-{amount}")

def withdraw():
     amount=int(input("Enter the amount: "))
     if amount<=data['Balance']:
          data['Balance']-=amount
          data['History'].append(f"withdraw-{amount}")
          print(f"withdraw-{amount}")
     else:
          print("insufsent fund")

def History():
     if History:
          for i in data['History']:
               print(i)
     else:
          print("No tran")

while True:
     print('1.Current balance')
     print('2.Deposit')
     print('3.Withdraw')
     print('4.History')
     print('0.Exit')

     ch=int(input("Enter your choice: "))

     if ch==1:
          current_balance()
     elif ch==2:
          deposit()
     elif ch==3:
          withdraw()
     elif ch==4:
          History()
     elif ch==0:
          break
     else:
          print("Invalid")

   

         
   
