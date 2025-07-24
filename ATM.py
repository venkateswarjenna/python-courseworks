data={
    1234:{"pin":123,"current balance":4000,"history":[]},
    5678:{"pin":123,"current balance":5000,"history":[]},
    9012:{"pin":123,"current balance":7000,"history":[]},
    }
print("Welcome to the Atm")
acc=int(input("Enter the account number: "))
pin=int(input("Enter the pin: "))

if acc in data and data[acc]["pin"]==pin:
    print("Login Succesful")
    
    print('''\n\nATM MENU
    1. Check Balance
    2. Deposit
    3. Withdraw
    4. View Transactions
    5. Exit''')
    op=int(input("select the option: "))

    if op==1:
        print(f"Current Balance: [data[acc]['current_balance']]")
    elif op==2:
        amount=int(input("Enter amount to dposited: "))
        data[acc]["history"].append(f"Deposited (amount)")
        print(f"Succesfully withdrawn (ammount)")
    elif op==3:
        

                             
