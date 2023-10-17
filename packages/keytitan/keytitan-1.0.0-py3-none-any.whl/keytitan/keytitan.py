import random
import string
import re

class KeyTitan:
    def __init__(self, length=12):
        """
        Initializes a KeyTitan object with an optional password length.

        Args:
            length (int, optional): The length of the generated password. Defaults to 12 characters.
        """
        self.length = length

    def generate_password(self):
        """
        Generates a random password with the specified length, following certain criteria.

        Returns:
            str: The generated password.
        Raises:
            ValueError: If the password length is less than 8 characters.
        """
        characters = ""
        if self.length < 8:
            raise ValueError("Password length must be at least 8 characters")
            
        # Define character sets for uppercase letters, lowercase letters, digits, and special characters.
        uppercase_chars = string.ascii_uppercase
        lowercase_chars = string.ascii_lowercase
        digit_chars = string.digits
        special_chars = string.punctuation

        # Make sure to include at least one character from each character set.
        password = (
            random.choice(uppercase_chars) +
            random.choice(lowercase_chars) +
            random.choice(digit_chars) +
            random.choice(special_chars)
        )

        # The remaining characters are randomly chosen from all character sets.
        all_chars = uppercase_chars + lowercase_chars + digit_chars + special_chars
        password += ''.join(random.choice(all_chars) for _ in range(self.length - 4))

        # Shuffle the password to randomize the character order.
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)

        return password

    def validate_password(self, password):
        """
        Validates a given password against certain criteria.

        Args:
            password (str): The password to validate.

        Returns:
            bool: True if the password is valid, False otherwise.
        """
        if not len(password) >= 8:
            print("Password length must be greater than 8.")
            return False
        if not re.search(r'[A-Z]', password):
            print("Password must include an uppercase letter.")
            return False
        if not re.search(r'[a-z]', password):
            print("Password must include a lowercase letter.")
            return False
        if not re.search(r'\d', password):
            print("Password must include a digit.")
            return False
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            print("Password must include a special character.")
            return False
        else:
            return True

if __name__ == "__main__":
    key_titan = KeyTitan(length=10)
    
    generated_password = key_titan.generate_password()
    print(f"Generated Password: {generated_password}")

    password_to_validate = "MyPass123!"
    if key_titan.validate_password(generated_password):
        print("Password is valid.")
    else:
        print("Password is not valid.")
