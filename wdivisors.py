def find_divisors(num):
    """Return a list of divisors of a positive integer."""
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

while True:
    try:
        number = input("Enter a positive number: ").strip()
        if not number:  # Check for empty input
            raise ValueError("Input cannot be empty.")
        number = int(number)
        if number <= 0:
            raise ValueError("Please enter a positive number.")
        print(f"Divisors of {number} are: {find_divisors(number)}")
        break
    except ValueError as e:
        print(e)
