# Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
def computegrade(score):
    # Check if the score is withing the valid range
    if score < 0.0 or score > 1.0:
        return("Bad score")
        
    # If the score is within the range, figure out the grade using a chain of elif statement
    elif score >= 0.9:
        return("A")
    elif score >= 0.8:
        return("B")
    elif score >= 0.7:
        return("C")
    elif score >= 0.6:
        return("D")
    else:
        return("F")

try:
    score = float(input("Enter Score: "))
    
    # Call the function and get the grade string back
    grade_result = computegrade(score)
    print(grade_result)
    
    
except:
    print("Bad score")