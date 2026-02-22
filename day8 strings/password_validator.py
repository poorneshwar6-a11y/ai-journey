def check_password(password):
    if len(password) < 8:
        return "Weak password (too short)"
    has_digit = False
    has_upper = False
    has_lower = False
    for ch in password:
        if ch.isdigit():
            has_digit = True
        elif ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
    if has_digit and has_upper and has_lower:
        return "Strong password"
    else:
        return "Weak password (missing required characters)"
password = input("Enter your password: ")
print(check_password(password))