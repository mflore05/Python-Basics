# Rewrite the pay program using try and except so that the program handles non-numeric input gracefully by printing a message and exiting the program.

try:
    # First, get the inputs and convert them to decimal numbers
    xh = float(input("Enter Hours: "))
    xr = float(input("Enter Rate: "))

    # Now, check if the employee worked overtime
    if xh > 40:
        reg_pay = 40 * xr
        # Calculate how many hours are overtime
        overtime_hours = xh - 40
        overtime_pay = overtime_hours * (xr * 1.5)
        xp = reg_pay + overtime_pay
    else:
        # if the hours are 40 or less, it's just the simple multiplication
        xp = xh * xr
    print("Pay: ", xp)

except:
    #If the user types the value in letters instead of using numbers, Python will panic above and jump here!
    print("Error, please enter numeric input")