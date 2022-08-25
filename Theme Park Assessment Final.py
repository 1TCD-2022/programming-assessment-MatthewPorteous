"""
Filename: Theme Park Assessment
Author: Matthew Porteous 1TDC
Start Date: 1/07/22
Description: This program is designed to help staff at a theme park to determine
which rides groups of people can go on depending on their height. Height
restrictions will be places on different rides for safety purposes. 
"""
rides = ["Teacups", "The Cyclone", "Vampire Cove", "The Slinger", "Slippery Slope", "The Mummies Tomb", "Candyland", "ZombieLand", "Superman", "Jurassic Park",]
height_restrictions = [147, 149, 150, 160, 165, 168, 169, 170, 175, 180]
VALID_MENU_CHOICE = [1, 2, 3, 4, 5, 5,7, 8, 9, 10]
applicable_rides = []
user_height_list = []
repeat_rides = True

while repeat_rides:
    print("""Welcome to the Fantastical Theme Park Height Checker!
    Before you enter our theme park we need to take your height!

    If you are in a group, we will find the individual height of your everyone
    in the group and decide which rides each person can go on!

    Groups with 10 people and under are allowed into the theme park""")
    try:
        applicable_rides = []
        user_choice = int(input("""Are you in a group today? If so enter the number of People in your group,if you aren't please enter  1:"""))
    #this will stop the user from entering the wrong value and will repeat until they enter a value input
        while user_choice > 10:
            user_choice = int(input("The max amount of people in a group is 10! Please enter a valid input:"))
    except ValueError:
        user_choice = int(input("Please enter a valid input:"))
        
        
                    
        

    if user_choice == 1:
                print("Please list off all the first names of the group!")
                user_name = str(input("What is your first name?"))#.isalpha is to make that so a string only uses alphabetical letters, as string can be also a number
                if user_name.isalpha():
                    try:
                        applicable_rides = []
                        print("Please enter the height of each person")
                        user_height = int(input("Please enter how tall {} is in CM. Round to a Whole Number:".format(user_name)))
                    except ValueError:
                            user_height = int(input("Please enter a valid height in CM. Round to a Whole Number:"))
                else:
                        user_name = str(input("Please enter a valid first name:"))    
                try:
                    user_height = int(input("Please enter how tall {} is in CM. Round to a Whole Number:".format(user_name)))
                except ValueError:
                    user_height = int(input("Please enter a valid height in CM. Round to a Whole Number:"))
#this massive chunk of code is comparing the user_height to the height restrictions and it will print out which ride the person can go on
                if user_height < height_restrictions[0]:
                    print("You can't ride anything !".format(rides[0]))
                    
                else:
                    for index in range(9):
                        if user_height >= height_restrictions[index]:
                            applicable_rides.append(rides[index])
                print("You can ride:")
                list(map(print, applicable_rides))


               
            
            
            
    elif user_choice != 1:
            #this for loop will loop as many times as there are people in a group. it will
            #also put all the heights of a user into a list    
            for index in range(user_choice):
                
                    print("Please list off all the first names of the group!")
                    user_name = str(input("What is your first name?"))#.isalpha is to make that so a string only uses alphabetical letters, as string can be also a number
                    if user_name.isalpha():
                        try:
                            applicable_rides = []
                            print("Please enter the height of each person")
                            user_height = int(input("Please enter how tall {} is in CM. Round to a Whole Number:".format(user_name)))
                        except ValueError:
                            user_height = int(input("Please enter a valid height in CM. Round to a Whole Number:"))
                    else:
                        user_name = str(input("Please enter a valid first name:"))
                        try:
                            print("Please enter the height of each person")
                            user_height = int(input("Please enter how tall {} is in CM. Round to a Whole Number:".format(user_name)))
                        except ValueError:
                            user_height = int(input("Please enter a valid height in CM. Round to a Whole Number:"))
                    if user_height < height_restrictions[0]:
                        print("You can't ride anything !".format(rides[0]))
                    
                    else:
                        for index in range(9):
                            if user_height >= height_restrictions[index]:
                                applicable_rides.append(rides[index])
                    print("You can ride:")
                    list(map(print, applicable_rides))

                        
         


                        
        
