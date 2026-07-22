# Lab incubators are often set un Celsius, but sometimes data arrives in Fahrenheit
xt = input("Enter Temperature in F: ")
xF = float(xt)
xC = (xF - 32) * 5 / 9
print("Temperature in Cº", xC)