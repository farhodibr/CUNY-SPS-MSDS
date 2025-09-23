# %% [markdown]
# 
# Q1: Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if statements and else statements print the user a message recommending a meal. For example, if the meal was breakfast, you could say something like, “How about some bacon and eggs?”
# The user may enter something else in, but you only have to respond to breakfast, lunch, or dinner.
# 

# %%
# dictionary of choices and suggestions
food_ideas = {'breakfast': 'scrambled eggs and coffee',
        'lunch': 'soup and burger',
        'dinner': 'pizza and wings'}

def user_input(menu):

    ''' 
    this function asks to type in one of choices 
    '''
    # input choice
    user_choice = input(f"Choices: breakfast, lunch, dinner. Please type-in your choice: ")

    return user_choice



def idea_suggestion():

    ''' 
    this function takes input from the user, and if it matches one of the keys in food_ideas returns suggestion
    '''
    # counter for tries
    counter = 3

    # loop for counter for tries 
    while counter > 0:
        user_choice_input = user_input(food_ideas)

        # verify input's value
        if user_choice_input in food_ideas.keys():

            # if input matches one of the keys print suggestion
            print(f"Suggestion for {user_choice_input} is {food_ideas[user_choice_input]}")
            break
        else:
            counter -= 1
            if counter > 0:
                print(f"Sorry, your input should match one of the choices"
                      f"You can try {counter} more times")
                
            else:
                print("Try again later") 

idea_suggestion()


    

# %% [markdown]
# Q2: The mailroom has asked you to design a simple payroll program that calculates a student employee’s gross pay, including any overtime wages. If any employee works over 20 hours in a week, the mailroom pays them 1.5 times their regular hourly pay rate for all hours over 20. 
# You should take in the user’s input for the number of hours worked, and their rate of pay.
# 
# 

# %%


def payroll_calculator():

    ''' 
    this function take student's hourly rate and calculates paycheck including if overtime is occuried
    '''
    # enter student's hours and payrate in float
    hours_worked = float(input("Please enter amount of worked hours"))
    hourly_pay = float(input("Please enter rate of pay"))
    print(f"Payrate ${hourly_pay}")
    # amount of hours with standard payrate
    standard_hours = 20
    
    # defaults for paycheck and output message
    weekly_pay = 0
    message = ''

    # make sure values are non-negative
    if hours_worked < 0 or hourly_pay <0:
        message = "Hours and payrate cannot be negative"
    else: # if not negative
        if hours_worked > standard_hours:    # calculate paycheck if overtime is occured
            
            overtime_hours = hours_worked - standard_hours
            ovrt_pay_hour = hourly_pay * 1.5
            
            std_pay_total = hourly_pay * standard_hours
            ovrt_pay_total = overtime_hours * ovrt_pay_hour

            weekly_pay = std_pay_total + ovrt_pay_total
            message = f"Total hours :{hours_worked} \n Standard pay: {std_pay_total} \nOvertime hours: {overtime_hours} \n Overtime pay: {ovrt_pay_total} \nPaycheck amount is ${weekly_pay}"
        else: # calculate regular paycheck if no overtime
            weekly_pay = hours_worked * hourly_pay
            message = f"Total hours: {hours_worked} \nPayrate: {hourly_pay} \n Employees check is {weekly_pay}"

    return weekly_pay, message

paycheck, message = payroll_calculator()

#print(paycheck)
print(message)

    



# %% [markdown]
# Q3: Write a function named times_ten. The function should accept an argument and display the product of its argument multiplied times 10.
# 

# %%
def times_ten(number):
    ''' function takes an argument and multiplies its value times 10'''
    outcome = number * 10
    print(f'{number} multiplied times 10 is equal to {outcome}')

times_ten(5)

# %% [markdown]
# SQ4: Find the errors, debug the program, and then execute to show the output.
# 
# ```python
# def main()
# 
#       Calories1 = input( "How many calories are in the first food?")
# 
#       Calories2 = input( "How many calories are in the first food?")
# 
#       showCalories(calories1, calories2)
# 
# def showCalories()   
# 
#    print(“The total calories you ate today”, format(calories1 + calories2,.2f))
# 
# ```
# In the cell below i fixed the errors and execution flow of code execution.  

# %%
def showCalories(input1, input2):   
   
   ''' function calculates and prints total amount of calories with two decimals '''

   print("The total calories you ate today", format(input1 + input2, '.2f'))

def main():
      ''' 
      function takes calories inputs and passes it to showCalories()

      '''
      
      calories1 = int(input( "How many calories are in the first food?"))

      calories2 = int(input( "How many calories are in the first food?"))

      return showCalories(calories1, calories2)

main()

# %% [markdown]
# Q5: Write a program that uses any loop (while or for) that calculates the total of the following series of numbers:
#          1/30 + 2/29 + 3/28 ............. + 30/1
# 

# %%
def calculate_special(num):

    ''' function uses two different methods to calculate the total of the following series of numbers:
         1/30 + 2/29 + 3/28 ............. + 30/1, 
         and as a bonus calculation also done with numpy.
         Each method returns same total value'''
    
    # creating list with lambda function
    num_range_list = list(map(lambda x: x+1, range(num)))

    # reverse of the list
    num_range_list_reversed = num_range_list[: : -1]
    print(num_range_list)
    print(num_range_list_reversed)

    # sum defaults
    total = 0
    total1 = 0

    # method 1
    for i, n in zip(num_range_list, num_range_list_reversed):
        
        total += i / n

    # method 2
    for i in num_range_list:
        index = num_range_list.index(i)

        total1 += i / num_range_list_reversed[index]

    # method 3 with numpy
    import numpy as np

    num_range_list_np = np.array(num_range_list)
    num_range_list_reversed_np = np.flip(num_range_list_np)

    num_range_list_divided = num_range_list_np / num_range_list_reversed_np

    total3 = float(np.sum(num_range_list_divided))
    # print(num_range_list_np, num_range_list_reversed_np, num_range_list_divided)

    

    return total, total1, total3




print(calculate_special(30))

# %% [markdown]
# Q6: Write a function that computes the area of a triangle given its base and height.
# 
# The formula for an area of a triangle is:
# 
# AREA = 1/2 * BASE * HEIGHT
# 
# For example, if the base was 5 and the height was 4, the area would be 10.
# 
# triangle_area(5, 4)   # should print 10
# 

# %%
def triangle_area(base, height):

    ''' function calculates and prints area of triangle '''
    
    area = base * height * 1/2
    print(f'Area of trianle with base of {base} and height of {height} is equal to {area}')

triangle_area(5, 4)


