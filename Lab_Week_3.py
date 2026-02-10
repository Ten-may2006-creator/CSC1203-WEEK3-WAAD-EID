##Q1##   
Password = input("Enter Your Password: ")
if Password == ("admin123"):
    print("Access Granted")
else :
    print("Access Denied!") 
###########################################
## Q2 ##
age = int(input("Enter Your Age: "))
if age < 13:
    print("Child")
elif age >= 13 and age <= 19
    print("Teen")
elif age >= 20 and age <= 59:
    print("Adult")
else:
    print("Senior")
#######################################
## Q3 ##
Number = int(input("Enter a Number:"))

if Number > 0 :
    print("Positive")
else: 
    print("Not Positive!")   

if Number >=10 and Number <= 50 :
    print("The Number is Between 10 and 50")
else: 
    print("The Number is NOT Between 10 and 50!")   

##################################################
##Q4##
color = input("Enter A Color :")
if color != "":
    match color:
        case "red":
            print ("Stop")
        case "yellow":
             print ("Get Ready")
        case "green":
            print("Go")
        case _:
            print("Unknown color")
else: 
    print("No input") 
#############################################
##Q5##
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

match choice:
    case 1:
        result = num1 + num2
        print("Result:", result)
    case 2:
        result = num1 - num2
        print("Result:", result)
    case 3:
        result = num1 * num2
        print("Result:", result)
    case 4:
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Division by zero")
    case _:
        print("Invalid choice")
#######################    
##Q6##
score = int(input("Enter student score: "))


if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"


match grade:
    case "A":
        print("Excellent! You passed with grade A")
    case "B":
        print("Very Good! You passed with grade B")
    case "C":
        print("Good! You passed with grade C")
    case "D":
        print("Passed, but you need improvement")
    case "F":
        print("Failed. Better luck next time")
