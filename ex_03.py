# Calculate a patient's Body Mass Index from clinical inputs
xw = input("Patient's weight in kg: ")
xW = float(xw)
xh = input("Patient's height in meters: ")
xH = float(xh)
xB = xW / (xH * xH)
print("Patient's BMI: ", xB)