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

# 4. Payslip Formatting
width = 40

# Header
header = "OFFICIAL PAYSLIP"
print(f"\n{header:=^{width}}")

# Divider using string multiplication
print("=" * width)

# Labels and Values
print(f"{'Hourly Rate:':<25}{'₹' + format(hourly_rate, ',.3f'):>15}")
print(f"{'Hours Worked:':<25}{hours_worked:>15}")
print(f"{'Tax:':<25}{str(tax * 100) + '%':>15}")
print(f"{'Gross Pay:':<25}{'₹' + format(gross, ',.3f'):>15}")
print(f"{'Tax Amount:':<25}{'₹' + format(tax, ',.3f'):>15}")

# Divider
print("=" * width)

# Net Pay
print(f"{'NET PAY:':<25}{'₹' + format(net_pay, ',.3f'):>15}")

# Footer
print("=" * width)

# 4. Data Type Validation
print("\n----- Data Type Validation -----")

print(f"Hourly Rate Type: {type(hourly_rate)}")
print(f"Hours Worked Type: {type(hours_worked)}")
print(f"Tax Type: {type(tax)}")
print(f"Gross Pay Type: {type(gross)}")
print(f"Net Pay Type: {type(net_pay)}")
