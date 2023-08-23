while True:
    try:
        number = int(input("Enter a number (or type 'exit' to quite): "))
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
    except ValueError:
        print("Please enter a valid number or type 'exit' to quit.")
    if input("Do you want to check another number? (yes/no): ").lower() != 'yes':
        break
    