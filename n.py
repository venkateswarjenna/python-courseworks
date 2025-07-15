n = int(input())# Height and width of the letter N

for row in range(n):
    for col in range(n):
        if col == 0 or col == n - 1 or col == row:
            print('*', end='')
        else:
            print(' ', end='')
    print()
