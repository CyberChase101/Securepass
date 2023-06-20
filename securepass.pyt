import random
import string

def generate_password(length=12, complex=True):
    characters = string.ascii_letters + string.digits + string.punctuation
    if not complex:
        characters = string.ascii_letters + string.digits
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt user for password length and complexity preference
password_length = int(input("Enter desired password length: "))
password_complexity = input("Do you want to include special characters? (Y/N): ").upper() == "Y"

# Generate and display the password
password = generate_password(length=password_length, complex=password_complexity)
print("Generated Password:", password)
