
import random

# Step 1: Password check
stored_password = "MySecretPassword"
user_input = input("Enter password: ")

if user_input != stored_password:
    print("Authentication failed!")
else:
    # Step 2: Generate OTP
    otp = random.randint(100000, 999999)
    print("OTP sent to your device:", otp)  # In real systems, send via SMS or email
    user_otp = int(input("Enter OTP: "))

    if user_otp == otp:
        print("Authentication successful! Access granted.")
    else:
        print("Authentication failed! Invalid OTP.")


##############################################################

Output
Enter password: MySecretPassword
OTP sent to your device: 529792
Enter OTP: 529792
Authentication successful! Access granted.