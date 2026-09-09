import random

# Generate OTP
otp = random.randint(100000, 999999)

print("Your OTP is:", otp)

# Ask user to enter OTP
user_otp = int(input("Enter the OTP: "))

if user_otp == otp:
    print("✅ OTP verified successfully!")
else:
    print("❌ Invalid OTP!")