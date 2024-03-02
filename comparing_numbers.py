'''
Write a program, that receives two numbers from the user, compares them
and returns the highest number.
1. Receive two numbers as integers
2. Create an if statement to compare two numbers.
'''

print("Hello! Tell me how much per hour you earn and how much your friend earns.\nGive hourly rate as integer")

while True:
    Your_hourly_rate = (input("My hourly rate is : "))
    Your_friend_hourly_rate = (input("My friend's hourly rate is: "))
    try:
        Your_hourly_rate = int(Your_hourly_rate)
        Your_friend_hourly_rate = int(Your_friend_hourly_rate)
        break
    except ValueError:
        print("Wrong input. You were asked to write down integer, no string, no floating-point number.\nGive me data one more time.")
        
if Your_hourly_rate > Your_friend_hourly_rate:
    print('Wow! You are doing great! And remember: work smarter, not harder :) ')
elif Your_friend_hourly_rate > Your_hourly_rate:
    print('Time to get to work!')
else:
    print('You both earn the same')

'''
-> using while loop let us serve cases when user gives any input except int
and come back to the beginning; numbers must be included in the loop
-> break - if input is correct, break the loop
'''
