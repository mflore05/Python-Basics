# Write a program to prompt for a score between 0.0 and 1.0. if the score is out of range, print an error message.

try:
    score = float(input("Enter Score: "))
    
    if score < 0.0 or score > 1.0:
        print("Bad score")
    # If the score is within the range, figure out the grade using a chain of elif statement
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
        
except:
    print("Bad score")