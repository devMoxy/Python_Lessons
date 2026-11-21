import string
import secrets

characters = string.ascii_letters + string.digits + string.punctuation

length = int(input("How long should the password be? "))

password = ""

for i in range(length):
    password += secrets.choice(characters)

print(f"Your password is {password}")