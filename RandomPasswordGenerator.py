import random
import string

def generate_password(length,use_letters=True,use_digits=True,use_symbols=True):
    characters=""
    if use_letters:
        characters+=string.ascii_letters

    if use_digits:
        characters+=string.digits

    if use_symbols:
        characters+=string.punctuation

    if not characters:
        return "Error: No character set selected!"
    password="".join(random.choice(characters)for _ in range(length))
    return password

print("Welcome to Random Password Generator!")
length=int(input("Enter password length: "))
use_letters=input("Include letters?(y/n): ").lower()=="y"
use_digits=input("Include numbers?(y/n): ").lower()=="y"
use_symbols=input("Include symbols?(y/n): ").lower()=="y"

print("\nGenerated Password:",generate_password(length,use_letters,use_digits,use_symbols))