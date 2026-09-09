# Electricity Bill Generator

print("=" * 45)
print("       ELECTRICITY BILL GENERATOR")
print("=" * 45)

name = input("Enter consumer name: ")
meter_no = input("Enter meter number: ")
units = float(input("Enter electricity units consumed: "))

# Calculate bill based on units
if units <= 100:
    bill = units * 3

elif units <= 200:
    bill = (100 * 3) + ((units - 100) * 5)

elif units <= 300:
    bill = (100 * 3) + (100 * 5) + ((units - 200) * 7)

else:
    bill = (100 * 3) + (100 * 5) + (100 * 7) + ((units - 300) * 10)

# Fixed charge
fixed_charge = 50

# Total bill
total_bill = bill + fixed_charge

# Display bill
print("\n")
print("=" * 45)
print("             ELECTRICITY BILL")
print("=" * 45)

print("Consumer Name :", name)
print("Meter Number  :", meter_no)
print("Units Consumed:", units)

print("-" * 45)
print(f"Energy Charges : ₹{bill:.2f}")
print(f"Fixed Charges  : ₹{fixed_charge:.2f}")
print("-" * 45)
print(f"TOTAL BILL     : ₹{total_bill:.2f}")
print("=" * 45)

print("       Thank you for using our service!")
print("=" * 45)