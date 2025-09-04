#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95
 
# Get the test scores.30

#this function checks if input value is an int
def numeric_input(text):
    while True:
        user_input = input(f" {text}: ").strip()
        try:
            value = int(user_input)
        except ValueError:
            print("Your input must be numeric. Try again")
            continue
        return value

#test0 = numeric_input("test 0")
#print(test0)

test1 = numeric_input("Enter the score for test 1") #changed the variable's type to int, so it can be used for calculations
test2 = numeric_input("Enter the score for test 2") #changed the variable's type to int
# declared missing variable test3 and added input 
test3 = numeric_input("Enter the score for test 3")



# Calculate the average test score.
#This line calculates the average
average = (test1 + test2 + test3 ) / 3 #the error was that only test3 was divided by 3, when average is calculated from sum of all variables divided by the total count of variables
# Print the average.
print('The average score is', average)
# If the average is a high score,
# congratulate the user.
if average == HIGH_SCORE:
    print('Congratulations!')
    print('That is a great average!')
else:
    print("Your average is lower than the high score")

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 

#get the length and width

length = numeric_input("Please enter the length of rectangle: ")
width = numeric_input("Please enter the width of rectangle: ")

#calculate the area of rectangle A = L * W
area = length * width
print(f"The area of rectangle is equal to: {area}")

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

name = input("Please enter your name: ")
age = numeric_input("Please enter your age: ")

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

print(f"Happy birthday, {name}! You are {age} years old today!")


