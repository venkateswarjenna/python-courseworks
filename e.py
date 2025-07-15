n = 5  # Height of the letter E

for row in range(n):
    for col in range(n):
        if row == 0 or row == n // 2 or row == n - 1 or col == 0:
            print('*', end='')
        else:
            print(' ', end='')
    print()
