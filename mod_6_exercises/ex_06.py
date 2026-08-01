# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters: hours and rate
def computepay(xh, xr):
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
        
    # Return the final calculated pay back to the caller
    return xp
    
try:
    # First, get the inputs and convert them to decimal numbers
    xh = float(input("Enter Hours: "))
    xr = float(input("Enter Rate: "))

    # Invoke the function and store the returned value in pay_result
    pay_result = computepay(xh, xr)
    
    print("Pay: ", pay_result)

except:
    #If the user types the value in letters instead of using numbers, Python will panic above and jump here!
    print("Error, please enter numeric input")