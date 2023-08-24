import time

def calculate_sum(n):
    return sum(range(1, n+1))

def fun_fact(n):
    if n == 7:
        return "Did you know? 7 is often considered a lucky number in various cultures!"
    elif n == 13:
        return "Interesting choice! 13 is often considered an unlucky number in many cultures."
    elif n % 2 == 0:
        return "You've chosen an even number!"
    else:
        return "You've chosen an odd number!"

def main():
    print("\033[1;34;40mWelcome to the Sum Calculator!\033[0m")  # Bold, Blue text
    print("-------------------------------")
    
    while True:
        try:
            n = int(input("\nEnter a number: "))
            time.sleep(1)  # Introducing a delay for a more interactive feel
            total = calculate_sum(n)
            print(f"\nThe sum of numbers from 1 to {n} is: \033[1;32;40m{total}\033[0m")  # Bold, Green text
            time.sleep(1)
            print("\033[1;33;40m" + fun_fact(n) + "\033[0m")  # Bold, Yellow text
            time.sleep(1)
            
            another = input("\nWould you like to calculate the sum for another number? (yes/no): ").lower()
            if another != 'yes':
                print("\n\033[1;34;40mThank you for using the Sum Calculator! Have a great day!\033[0m")
                break
        except ValueError:
            print("\033[1;31;40mOops! That's not a valid number. Please try again.\033[0m")  # Bold, Red text

if __name__ == "__main__":
    main()
