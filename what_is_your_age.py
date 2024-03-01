'''
1. Create a variable that stores input that aska the user's age.
2.Create an if statement that checks the age provided. If the age is grater
than 18, display the message "access granted". If the age is under 18, display
"access denied"
Cast the data type of the variable to integer.
'''
while True:
    print('Hello! What is your age?')
    age = input("Hello! I'm: ")

    try:
        age = int(float(age))
        break
    except ValueError:
        print("Hey, what's wrong with you? Give me your age in number!")

'''
-> using while loop let us serve cases when user gives string as age and came back to 
first question about age
-> age = int(float(age)) let us process case when user input floating-point
number and then convert it to integer as stands in task
-> break - if input is correct, break the loop
'''

if age > 18:
    print("You are an adult, responsible man. Access granted.")
elif age < 18:
    print('Sorry, too young. Access denied, go to mummy.')
else:
    print("Don't know what to do with you...")