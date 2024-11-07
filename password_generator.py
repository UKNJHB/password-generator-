import string
import random

first_run = True  # Variable to track the first run

while True:
    if first_run:
        print("Welcome to the Password Generator")
        first_run = False  # Set to False after the first run
    
    # Loop until valid input for total_number
    while True:
        try:
            total_number = int(input("Enter the total number of characters in your password: ")) 
            break  # Break the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    # Loop until valid input for letter
    while True:
        try:
            letter = int(input("Enter the number of letters in the password: ")) 
            break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    # Loop until valid input for digit
    while True:
        try:
            digit = int(input("Enter the number of numbers in the password: "))
            break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    # Loop until valid input for symbol
    while True:
        try:
            symbol = int(input("Enter the number of symbols in the password: "))
            break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    # Check if the sum matches the total number
    if total_number == sum([letter, digit, symbol]):
        random_letter = random.choices(string.ascii_letters, k=letter)
        random_digit = random.choices(string.digits, k=digit)
        random_symbol = random.choices(string.punctuation, k=symbol)

        password_list = random_letter + random_digit + random_symbol
        random.shuffle(password_list)
        password = "".join(password_list)
        print("Generated Password:", password)

        another = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Thank you for using the Password Generator!")
            break
    else:
        print("Invalid input, the sum of letters, digits, and symbols doesn't match the total number.")
        print("Please try again.\n")  # Prompt to try again

    
