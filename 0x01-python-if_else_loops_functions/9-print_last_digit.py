def print_last_digit(number):
    last_digit = abs(number) % 10  # Get absolute value to handle -ve nums
    print(last_digit, end="")
    return last_digit
