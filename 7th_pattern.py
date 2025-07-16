for row in range(5):
    for col in range(row):
        print('',end='')
    for col1 in range(5-row):
        print('*',end='')
    print()
