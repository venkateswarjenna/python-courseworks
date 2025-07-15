n = 10  # Must be an odd number ≥ 3

for row in range(n):
    for col in range(n * 2 - 1):
        if col == row or col == (2 * n - 2 - row):
            print('*', end='')
        else:
            print(' ', end='')
    print()
