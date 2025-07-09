def check_password_strength():
    password = input("Enter your password: ")

    if len(password) < 8:
        print("Password must be at least 8 character long. ")
        return 
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter. ")
        return
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter. ")
        return
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit. ")
        return
    if not any(char in "~!@#$%^&*" for char in password):
        print("Password must contain at least one special character.")
        return
    
    print("✅ Password is strong and valid!")

check_password_strength()

# **************************************************************


