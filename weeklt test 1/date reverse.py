n=input().lower()
v='aeiou'
for i in n:
    if i in v:
        n=n.replaces(i,'*')
print(n)
