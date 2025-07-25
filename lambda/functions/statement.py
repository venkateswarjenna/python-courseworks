def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b


stmt=input()
a=None
b=None
op=None

for i in stmt:
    if not i.isdigit():
        a,b=stmt.split(i)
        op=i

a,b=int(a),int(b)
print(a,b,op)

if op=='+':
    print(add(a,b))
elif op=='-':
    print(sub(a,b))
elif op=='*':
    print(mul(a,b))
elif op=='/':
    print(div(a,b))
else:
    print("invalid")