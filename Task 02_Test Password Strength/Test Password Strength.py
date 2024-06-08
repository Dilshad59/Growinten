import re

def password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = bool(re.search(r'[A-Z]', password))
    lower_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'[0-9]', password))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

    if score == 5:
        strength = 'Very Strong'
    elif score == 4:
        strength = 'Strong'
    elif score == 3:
        strength = 'Moderate'
    elif score == 2:
        strength = 'Weak'
    else:
        strength = 'Very Weak'

    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long")
    if not upper_criteria:
        feedback.append("Password should include at least one uppercase letter")
    if not lower_criteria:
        feedback.append("Password should include at least one lowercase letter")
    if not digit_criteria:
        feedback.append("Password should include at least one digit")
    if not special_criteria:
        feedback.append("Password should include at least one special character")
    
    return strength, feedback

def main():
    password = input("Enter a password: ")
    strength, feedback = password_strength(password)
    
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback to improve your password:")
        for tip in feedback:
            print(f" - {tip}")

if __name__ == "__main__":
    main()
