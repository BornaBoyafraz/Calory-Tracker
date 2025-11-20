#LOADING MODULES
# os: Used for file operations like checking if files exist and removing files
# time: Used for delays and sleep functions
# Calories_Functions: Used for functions written inside it

import os
import time
import sys
import app_state

#navigating to the new path
sys.path.append("/App_Functions")
from App_Functions import Calories_Functions
from App_Functions import typing_functions

#file
# Name of the food database file that stores meal names and their calorie values
# Get user name
# Gets the user's name and formats it (lowercase, spaces replaced with underscores)
# This formatted name is used as the filename for storing user data
# user_name = typing_functions.type_input("Enter your first and last name: ").strip().lower().replace(" ", "_")
# file_name = user_name + ".txt"  # Create filename from user name
# foodData = 'foods.txt'

username = app_state.user_name
file_name = app_state.file_name
foodData = app_state.foodData


#We have the file and we should load it
# Check if user's data file already exists
if os.path.exists(app_state.user_data_file_path(file_name)):
    # Existing user - load their data and show menu
    typing_functions.type_print("found your file. Loading it...")
    
    #loading the values (just to verify file is readable)
    Calories_Functions.load_value(username + '.txt')
    time.sleep(1)
    typing_functions.type_print("Your data has been loaded successfully.")

    #load the user choice function (show main menu)
    Calories_Functions.UserRequest.User_Choice()
    
#We don't have the file, let's make a new one
# New user - need to set up their profile
else:
    # Memory storage for user data
    typing_functions.type_print('creating new file...')
    time.sleep(2)
    values = {}  # Start with empty dictionary

    # loop to get user input
    # Keep asking until user provides valid data and chooses to continue
    while True:
        # Get user's calorie goals for rest days and workout days
        restDay = int(typing_functions.type_input("How many calories do you wanna take on rest days?: "))
        workoutDay = int(typing_functions.type_input("How many calories do you wanna take on workout days?: "))

        # Build the user data dictionary step by step
        values["user_name"] = username
        Calories_Functions.save_value(str(values), file_name)  # Save after each addition

        values["Rest Day Calories"] = restDay
        Calories_Functions.save_value(str(values), file_name)  # Update file with rest day calories

        values["Workout Day Calories"] = workoutDay
        Calories_Functions.save_value(str(values), file_name)  # Update file with workout day calories

        typing_functions.type_print("Saving your data...")
        time.sleep(5)
        typing_functions.type_print("Your data has been saved successfully.")

        # Ask if user wants to continue to main menu or exit
        continue_choice = typing_functions.type_input("Do you want to continue? (yes/no): ").strip().lower()

        if continue_choice == "yes":
            Calories_Functions.UserRequest.User_Choice()  # Go to main menu
            break  # Exit the while loop
        elif continue_choice == "no":
            Calories_Functions.closing_program()  # Exit the program
        else:
            typing_functions.type_print("Invalid choice. Please try again.")  # Ask again

