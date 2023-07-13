import sys

# Check if the number of command line arguments is correct
if len(sys.argv) != 2:
    print("Usage: python program_name.py <number>")
    sys.exit(1)

# Retrieve the number from the command line argument
num = int(sys.argv[1])

if num % 2 != 0:
    print("The number is odd.")
else:
    print("The number is not odd (i.e., it is even or zero).")
