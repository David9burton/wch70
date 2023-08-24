import number_checker

num = int(input("Enter a number to check if it's even or odd: "))

result = number_checker.is_even(num)
if result:
    print(f"The number {num} is even.")
else:
    print(f"The number {num} is odd.")