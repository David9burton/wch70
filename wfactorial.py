def factorial(n):
    """Return the factorial of a non-negative integer."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

while True:
    try:
        number = input("Enter a non-negative number: ").strip()
        if not number:  # Check for empty input
            raise ValueError("Input cannot be empty.")
        number = int(number)
        if number < 0:
            raise ValueError("Please enter a non-negative number.")
        print(f"Factorial of {number} is {factorial(number)}")
        break
    except ValueError as e:
        print(e)
