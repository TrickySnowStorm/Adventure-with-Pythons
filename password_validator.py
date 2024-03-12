'''
Write a function called password_validator. The function
asks the user to enter a password. A valid password should have
at least one upper letter, one lower letter, and one
number. It should not be less than 8 characters long. When
the user enters a password, the function should check if the
password is valid. If the password is valid, the function should
return the valid password. If the password is not valid, the
function should tell the users the errors in the password and
prompt the user to enter another password. The code should
only stop once the user enters a valid password. (use while loop)
'''

def password_validator(password):
    while True:
        errors = []
        if not any(i.isupper() for i in password):
            errors.append("Error. Password must have at least 1 uppercase letter.")
        if not any(i.islower() for i in password):
            errors.append("Error. Password must have at least 1 lowercase letter.")
        if not any(i.isdigit() for i in password):
            errors.append("Error. Password must have at least 1 digit.")
        if len(password) < 8:
            errors.append("Error. Password must have at least 8 characters.")

        if errors:
            print('\n'.join(errors))
            password = input('Please, enter password again: ')
            
        else:
            return 'That is ok. Your password: ' + password


password = input("Please enter the password.\nIt should have at least one upper letter, one lower letter, one number and should not be less than 8 characters long.\nPassword: ")
check = password_validator(password)
print(check)