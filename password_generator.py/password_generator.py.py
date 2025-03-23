import secrets
import string

def generate_secure_password(length=12, include_uppercase=True, include_special=True, include_digits=True):
    """
    Generates a cryptographically secure password.
    
    Parameters:
        length (int): Length of the password (minimum 8 for security).
        include_uppercase (bool): Whether to include uppercase letters.
        include_special (bool): Whether to include special characters.
        include_digits (bool): Whether to include digits.

    Returns:
        str: A securely generated password.
    """

    # Enforce minimum length requirement
    if length < 8:
        raise ValueError("Password length must be at least 8 characters for security.")

    # Define character sets
    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ""
    special = string.punctuation if include_special else ""
    digits = string.digits if include_digits else ""

    # Ensure at least one character type is selected
    all_characters = lower + uppercase + special + digits
    if not all_characters:
        raise ValueError("At least one character type must be selected.")

    # Ensure at least one of each selected character type
    required_characters = []
    if include_uppercase:
        required_characters.append(secrets.choice(uppercase))
    if include_special:
        required_characters.append(secrets.choice(special))
    if include_digits:
        required_characters.append(secrets.choice(digits))

    # Fill the rest of the password length with random characters
    remaining_length = length - len(required_characters)
    password = required_characters + [secrets.choice(all_characters) for _ in range(remaining_length)]

    # Shuffle the password to remove predictable patterns
    secrets.SystemRandom().shuffle(password)

    return "".join(password)

# Example usage
if __name__ == "__main__":
    try:
        # Taking user input for customization
        length = int(input("Enter password length (min 8): ").strip())
        include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
        include_special = input("Include special characters? (yes/no): ").strip().lower() == "yes"
        include_digits = input("Include digits? (yes/no): ").strip().lower() == "yes"

        # Generate the password
        password = generate_secure_password(length, include_uppercase, include_special, include_digits)
        print("\n🔐 Generated Secure Password:", password)

    except ValueError as e:
        print("\n❌ Error:", e)
    except Exception as e:
        print("\n⚠️ Unexpected Error:", e)
        
        
        
 #Convert this into a Django/Flask API or Vue.js frontend for better usability.