data={
'prasanth@gmail.com':'123@',
'Dinesh@gmail.com':'789!',
'Sanjay@gmail.com':'456',
}

email,pwd=input("Enter the email and pwd:").split()
print(email,pwd)
if data.get(email)==pwd:
    print('login successful')        
else:
    print('Invalid login')
   
        
