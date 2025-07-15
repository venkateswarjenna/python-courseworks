def check_odd_even(n):
    if 1 <= n <= 100:
        if n % 2 == 0:
            return "even"
        else:
            return "odd"
    else:
        return "Input out of range (1 to 100)"
