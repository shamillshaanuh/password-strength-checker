import re
import random
import string

def generate_strong_password(length=12):
    """Generate a random strong password with letters, digits, and special characters."""
    if length < 8:
        length = 8  # minimum strength
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?/~"
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def check_password_strength(password):
    suggestions = []

    length_check = len(password) >= 8
    uppercase_check = re.search(r'[A-Z]', password) is not None
    lowercase_check = re.search(r'[a-z]', password) is not None
    digit_check = re.search(r'[0-9]', password) is not None
    special_check = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    score = sum([length_check, uppercase_check, lowercase_check, digit_check, special_check])

    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    if not length_check:
        suggestions.append("Use at least 8 characters.")
    if not uppercase_check:
        suggestions.append("Add at least one uppercase letter (A-Z).")
    if not lowercase_check:
        suggestions.append("Add at least one lowercase letter (a-z).")
    if not digit_check:
        suggestions.append("Include at least one number (0-9).")
    if not special_check:
        suggestions.append("Include at least one special character (e.g., @, #, $, etc.)")

    return strength, suggestions

# --- Main CLI ---
print("\n🔐 Password Strength Checker 🔐\n")
password = input("🔑 Enter your password (or type 'gen' to get a strong one): ")

if password.lower() == 'gen':
    generated = generate_strong_password()
    print(f"\n🔒 Generated Strong Password: {generated}")
    password = generated

strength, suggestions = check_password_strength(password)

print(f"\n✅ Strength: {strength}")
if suggestions:
    print("💡 Suggestions to improve:")
    for tip in suggestions:
        print("- " + tip)
else:
    print("🎉 Your password is strong!")

