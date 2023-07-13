def is_odd(num):
    if num % 2 != 0 and num != 0:
        return 2
    else:
        return 1
print(is_odd(4))  # Output: 1 (Even)
print(is_odd(7))  # Output: 2 (Odd)
print(is_odd(0))  # Output: 1 (Even)
print(is_odd(-12))  # Output: 1 (Even)
