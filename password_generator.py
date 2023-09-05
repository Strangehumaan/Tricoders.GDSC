import random
import string

def generate_password(length):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Generate a random password of length 10
password = generate_password(10)
print("Random Password:", password)
