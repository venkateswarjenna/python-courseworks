'''
def feed():
    return l

l=['1..100','101..200','201..300','302..400']
print(feed(l))
'''
'''
def feed(l):
    for i in l:
        yield i
            
l=['file1','file2','file3','file4']
load = feed(l)
print(next(load))
print(next(load))
print(next(load))
print(next(load))
'''
'''
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

gen = count_up_to(3)

for num in gen:
    print(num)

'''
