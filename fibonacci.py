def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

try:
    count = int(input("How many Fibonacci numbers would you like to see? "))
    print(f"The first {count} numbers of the Fibonacci sequence are:")
    print(fibonacci(count))
except ValueError:
    print("Please enter a valid number.")
    