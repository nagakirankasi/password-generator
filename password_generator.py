import random
import string

def generate_password(length, use_digits=True, use_special_chars=True):
    """Generate a secure password based on user preferences."""
    
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Generated Password:", generate_password())
