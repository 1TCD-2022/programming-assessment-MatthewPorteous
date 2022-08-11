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
VALID_MENU_CHOICE = [1, 2, 3, 4, 5, 5,7, 8, 9, 10]
applicable_rides = []
user_height_list = []



print("""Welcome to the Fantastical Theme Park!
Before you enter our theme park we need to take your height!

If you are in a group, we will find the individual height of your everyone
in the group and decide which rides each person can go on!

Groups with 10 people and under are allowed into the theme park""")
try:
    user_choice = int(input("""Are you in a group today? If so enter the number of People in your group,if you aren't please enter  1:"""))
#this will stop the user from entering the wrong value and will repeat until they enter a value input
    if user_choice > 10:
        user_choice = int(input("The max amount of people in a group is 10! Please enter a valid input:"))
except ValueError:
    user_choice = int(input("Please enter a valid input:"))
    if user_choice > 10:
        user_choice = int(input("The max amount of people in a group is 10! Please enter a valid input:"))
    

if user_choice == 1:
    
            print("Please tell us your first names!")
            user_name = str(input("What is your first name?")).isalpha()#.isalpha is to make that so a string only uses alphabetical letters, as string can be also a number
            if user_name == False:
                user_name = str(input("Please enter a valid first name:"))
            try:
                user_height = int(input("Please enter how tall {} is in CM. Round to a Whole Number:".format(user_name)))
            except ValueError:
                user_height = int(input("Please enter a valid height in CM. Round to a Whole Number:"))

           
        
        
        
elif user_choice != 1:
        #this for loop will loop as many times as there are people in a group. it will
        #also put all the heights of a user into a list    
        for index in range(user_choice):
            
                print("Please list off all the first names of the group!")
                user_name = str(input("What is your first name?")).isalpha()#.isalpha is to make that so a string only uses alphabetical letters, as string can be also a number
                if user_name == False:
                    user_name = str(input("Please enter a valid first name, Also do not enter someones name who has already been entered:"))
                try:
                    print("Please enter the heights of each individual person")
                    user_height = int(input("Please enter how tall {} is in CM. Round to a Whole Number:".format(user_name)))
                except ValueError:
                    user_height = int(input("Please enter a valid height in CM. Round to a Whole Number:"))
         


                    
    
