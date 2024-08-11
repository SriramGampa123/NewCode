print("Quiz Game")
score = 0

print("1. Who invented python?")
a1 = input("Enter the answer")
if a1 == "Guido Van Rossum":
    score += 4
    
print("2. What is the exntension of python?")
a1 = input("Enter the answer")
if a1 == ".py":
    score += 3
    
print("3.What is the fullform of 'PEP'?")
a1 = input("Enter the answer")
if a1 == "Python Enhancement Program":
    score += 3
    
print("You got" + str(score) + "/10")