import secrets
import string


characters = string.ascii_uppercase + string.ascii_lowercase

include_digits = input("Do you want to generate digits in your password? y/N: ")
if include_digits == "y":
    characters += string.digits

include_special_chars = input(
    "Do you want to generate special characters in your password? y/N: "
)
if include_special_chars == "y":
    characters += string.punctuation

while True:
    try:
        password_length = int(
            input("Enter the length of the password you want to generate: ")
        )

        if password_length > 0:
            break
        else:
            print("Please enter a positive number.")

    except ValueError:
        print("Please enter a valid number.")

password = ""

for _ in range(password_length):
    password += secrets.choice(characters)

print(password)