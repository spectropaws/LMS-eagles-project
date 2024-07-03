import secrets
import string
import re

# Get token that generates random string
def get_token(length=32):
    characters = string.ascii_letters + string.digits + string.punctuation
    token = ''.join(secrets.choice(characters) for i in range(length))
    return token

# Validation function
def validate_username_password(username, password):
    username_valid = bool(re.match(r'^[a-z]+$', username))
    password_valid = bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d!@#$%^&*(),.?":{}|<>]{8,}$', password))
    return username_valid and password_valid
