import unittest
from keytitan import keytitan

class TestKeyTitan(unittest.TestCase):

    def test_generate_password(self):
        key_titan = keytitan.KeyTitan(length=12)
        generated_password = key_titan.generate_password()

        # Check if the generated password has the correct length
        self.assertEqual(len(generated_password), 12)

        # Check if the generated password contains at least one uppercase letter
        self.assertTrue(any(c.isupper() for c in generated_password))

        # Check if the generated password contains at least one lowercase letter
        self.assertTrue(any(c.islower() for c in generated_password))

        # Check if the generated password contains at least one digit
        self.assertTrue(any(c.isdigit() for c in generated_password))

        # Check if the generated password contains at least one special character
        special_chars = "!@#$%^&*(),.?\":{}|<>"
        self.assertTrue(any(c in special_chars for c in generated_password))

    def test_validate_password(self):
        key_titan = keytitan.KeyTitan(length=12)

        # Valid password
        valid_password = "ValidPass123!"
        self.assertTrue(key_titan.validate_password(valid_password))

        # Invalid password: Too short
        short_password = "Short1!"
        self.assertFalse(key_titan.validate_password(short_password))

        # Invalid password: Missing uppercase letter
        no_uppercase_password = "nopass123!"
        self.assertFalse(key_titan.validate_password(no_uppercase_password))

        # Invalid password: Missing lowercase letter
        no_lowercase_password = "NOPASS123!"
        self.assertFalse(key_titan.validate_password(no_lowercase_password))

        # Invalid password: Missing digit
        no_digit_password = "NoDigitPass!"
        self.assertFalse(key_titan.validate_password(no_digit_password))

        # Invalid password: Missing special character
        no_special_char_password = "NoSpecialChar123"
        self.assertFalse(key_titan.validate_password(no_special_char_password))

if __name__ == '__main__':
    unittest.main()
