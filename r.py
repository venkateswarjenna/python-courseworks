n = 7  # Height of the letter R

for row in range(n):
    for col in range(n):
        if col == 0 or row == 0 or row == n // 2:
            print('*', end='')
        elif col == n - 1 and row < n // 2:
            print('*', end='')
        elif row - col == n // 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()
