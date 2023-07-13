def add_last_digits(num1, num2):
    last_digit_1 = abs(num1) % 10
    last_digit_2 = abs(num2) % 10
    return last_digit_1 + last_digit_2
print(add_last_digits(267, 154))     # Output: 11
print(add_last_digits(267, -154))    # Output: 11
print(add_last_digits(-267, 154))    # Output: 11
print(add_last_digits(-267, -154))   # Output: 11
