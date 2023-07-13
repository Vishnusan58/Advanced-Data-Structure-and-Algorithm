def get_second_last_digit(num):
    num = abs(num)
    if num < 10:
        return -1
    else:
        num = num // 10
        return num % 10
print(get_second_last_digit(197))   # Output: 9
print(get_second_last_digit(-197))  # Output: 9
print(get_second_last_digit(5))     # Output: -1
