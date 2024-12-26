# Password Strength Checker

A simple Python script to evaluate the strength of a password based on various criteria, including length, digit, uppercase, lowercase, special character, and uniqueness against common passwords.

## Features

- Checks password length (minimum 12 characters)
- Checks for the presence of digits
- Checks for the presence of uppercase letters
- Checks for the presence of lowercase letters
- Checks for the presence of special characters
- Checks for uniqueness against a list of common passwords

## Requirements

- Python 3.6 or higher

## Usage

1. Clone the repository:
   
       git clone https://github.com/Mohansaikrishna1601/Brainwave_Matrix_Intern-Task02.git
       cd Brainwave_Matrix_Intern-Task02

2. Run the script:

       python3 PasswordStrengthChecker.py

3. Enter a password when prompted to check its strength.

### Example
    Enter a password to check its strength: MySecureP@ssw0rd!

    🔒 Password Strength: Very Strong

    📝 Detailed Criteria:
    ==============================

    ✅ Length (min 12 chars)
    ✅ Digit
    ✅ Uppercase
    ✅ Lowercase
    ✅ Special Character
    ✅ Uniqueness
    ==============================


### How It Works

The script evaluates the password based on the following criteria:

    Length: Must be at least 12 characters long.

    Digit: Must contain at least one digit.

    Uppercase: Must contain at least one uppercase letter.

    Lowercase: Must contain at least one lowercase letter.

    Special Character: Must contain at least one special character (e.g., !, @, #).

    Uniqueness: Must not be a common password.

The overall strength is calculated based on the number of criteria met:

    Very Strong: All criteria met.

    Strong: 5 criteria met.

    Moderate: 3-4 criteria met.

    Weak: 2 criteria met.

    Very Weak: 0-1 criteria met.


## Author
Mohan Sai Krishna G M
