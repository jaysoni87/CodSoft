import random
import string

def password_generator():
    print("Welcome to the Password Generator!")

    # Prompt user for password length
    try:
        length = int(input("Enter the desired length of the password (minimum 8): "))
        if length < 8:
            print("Password length should be at least 8 characters for better security.")
            return
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    # Define character pools
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character pools
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure at least one character from each category
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Convert list to string and display the password
    generated_password = ''.join(password)
    print(f"Generated Password: {generated_password}")

# Run the password generator
password_generator()
