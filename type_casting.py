# 1. User Acquisition
hourly_rate_input = input("Enter hourly rate: ")
hours_worked_input = input("Enter hours worked: ")
tax_input = input("Enter tax percentage (e.g., 0.2 for 20%): ")

# 2. Casting
hourly_rate = float(hourly_rate_input)
hours_worked = int(hours_worked_input)
tax = float(tax_input)/100

print(f"Hourly Rate: {hourly_rate}")
print(f"Hours Worked: {hours_worked}")
print(f"Tax: {tax * 100}%")

# 3. Calculation
gross = hourly_rate * hours_worked
net_pay = gross - (gross * tax)

print(f"Gross Pay: {gross:.2f}")
print(f"Net Pay: {net_pay:.2f}")

# 4. Validation
print(f"Type of hourly_rate: {type(hourly_rate)}")
print(f"Type of hours_worked: {type(hours_worked)}")
print(f"Type of tax: {type(tax)}")
print(f"Type of gross_pay: {type(gross)}")
print(f"Type of net_pay: {type(net_pay)}")