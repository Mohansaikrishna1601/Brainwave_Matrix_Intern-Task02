import re

def password_strength(password):
    # Criteria
    length_criteria = len(password) >= 12
    digit_criteria = re.search(r"\d", password) is not None
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Evaluate password
    strength = {
        "Length (min 12 chars)": length_criteria,
        "Digit": digit_criteria,
        "Uppercase": uppercase_criteria,
        "Lowercase": lowercase_criteria,
        "Special Character": special_char_criteria
    }

    # Calculate overall strength
    num_criteria_passed = sum(value for value in strength.values())

    if num_criteria_passed == 5:
        strength["Overall Strength"] = "Very Strong"
    elif num_criteria_passed >= 4:
        strength["Overall Strength"] = "Strong"
    elif num_criteria_passed >= 3:
        strength["Overall Strength"] = "Moderate"
    elif num_criteria_passed >= 2:
        strength["Overall Strength"] = "Weak"
    else:
        strength["Overall Strength"] = "Very Weak"
    
    return strength

def display_strength(strength):
    print("\n🔒 Password Strength: ", strength["Overall Strength"])
    print("\n📝 Detailed Criteria:")
    print("="*30)
    
    for criterion, passed in strength.items():
        if criterion != "Overall Strength":
            status = "✅" if passed else "❌"
            print(f"\n{status} {criterion}")
            if not passed:
                if criterion == "Length (min 12 chars)":
                    print("  ➡️ Try making your password longer (minimum 12 characters).")
                elif criterion == "Digit":
                    print("  ➡️ Add at least one digit.")
                elif criterion == "Uppercase":
                    print("  ➡️ Include at least one uppercase letter.")
                elif criterion == "Lowercase":
                    print("  ➡️ Include at least one lowercase letter.")
                elif criterion == "Special Character":
                    print("  ➡️ Add at least one special character (e.g., !, @, #).")
    print("="*30)

# Example Usage
password = input("Enter a password to check its strength: ")
result = password_strength(password)
display_strength(result)
