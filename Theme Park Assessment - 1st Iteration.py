"""
Filename: Theme Park Assessment
Author: Matthew Porteous 1TDC
Start Date: 1/07/22
Description: This program is designed to help staff at a theme park to determine
which rides groups of people can go on depending on their height. Height
restrictions will be places on different rides for safety purposes. 
"""
rides = ["The Cyclone", "Vampire Cove", "The Slinger", "Slippery Slope", "The Mummies Tomb"]
height_restrictions = [145, 150, 150, 170, 175]
applicable_rides = []
user_height_list = []
try:
    user_choice = int(input("""
Are you in a group today?
If so enter the number of People in your group,if you aren't please enter  1:
"""))
#this will stop the user from entering the wrong value and will repeat until they enter a value input
except ValueError:
    user_choice = int(input("""
Please enter a valid number:"""))    

if user_choice == "1":
    user_height = int(input("Please enter how tall you are in cm"))
    user_height_list.append(user_height)
    """for index in height_restrictions:
        if user_height_list >= height_restrictions[index]:
            print("You can on all of these rides! : {}".format(height_restrictions[0,index]))"""
    
if user_choice != "1":
    #this for loop will loop as many times as there are people in a group. it will
    #also put all the heights of a user into a list    
    for index in range(user_choice):
        user_height = int(input("Please enter how tall you are in cm. Please round your height to a whole number."))
        user_height_list.append(user_height)
        """for index in range(5):
         if user_height > height_restrictions[index]:
            applicable_rides.append(rides[0,5])
            print("You can on all of these rides! : {}".format(applicable_rides[0,index]))"""

                    
    
