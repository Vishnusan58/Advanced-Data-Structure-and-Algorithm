def addLastDigits(input1, input2):
    last_digit_1 = abs(input1) % 10
    last_digit_2 = abs(input2) % 10
    return last_digit_1 + last_digit_2
print(addLastDigits(267, 154))     # Output: 11
print(addLastDigits(267, -154))    # Output: 11
print(addLastDigits(-267, 154))    # Output: 11
print(addLastDigits(-267, -154))   # Output: 11
