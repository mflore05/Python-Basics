# Ask a researcher how many cells they see in one square of a grid, then calculate the total for a 4-square grid
xc = input("Enter cell count for one square: ")
xC = int(xc)

# xT will represent the whole number of cells counter in a square multiplied by 4
xT = xC * 4
print("Total estimated cell count is: ", xT)