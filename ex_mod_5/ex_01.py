# Rewrite the pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

# First, get the inputs and convert them to decimal numbers
xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
xH = float(xh)
xR = float(xr)

# Now, check if the employee worked overtime
if xH > 40:
    reg_pay = 40 * xR
    # Calculate how many hours are overtime
    overtime_hours = xH - 40
    overtime_pay = overtime_hours * (xR * 1.5)
    xp = reg_pay + overtime_pay
else:
    # if the hours are 40 or less, it's just the simple multiplication
    xp = xH * xR
print("Pay: ", xp)