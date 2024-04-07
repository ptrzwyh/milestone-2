# def password_system():
#     numOfChance = 3
#     password = "123456"

#     global access

#     while numOfChance > 0:
#         userInput = str(input("Please enter the password to access Maintenance Adjustment Mode: "))
       
#         if userInput == password:
#                 access = True
#                 break
#         else:
#             numOfChance -= 1
#             print(f"""Your password is incorrect
#                   Please try again
#                   Attempt left {numOfChance}""")
#             access = False
#     return access


# def maintenance_adjustment_mode():


#     while True:
#         try:
#             access = password_system()
#             if access:
#                 modification_system()
 
#             else:
#                 selection_of_mode()


#         except KeyboardInterrupt:
#             print("""-> Keyboard Interrupt
#                   --Exit to the Menu--""")
#             selection_of_mode()

# def modification_system():
#     print("""Choose the mode you need to modified:
#             1. Normal Operation Mode
#             2. Maintenance Adjustment Mode
#             3. Data Observation Mode""")

# def menu ():
#     print("""Choose the mode you need according to its number
#             1. Normal Operation Mode
#             2. Maintenance Adjustment Mode
#             3. Data Observation Mode""")
#     while True:
#         try:
#             selectedMode = int(input("Select your mode:"))
#             if selectedMode == (1 or 2 or 3):
#                 break
#             else:
#                 print("Please enter number between 1 and 3")


#         except ValueError:
#             print("Please select the mode you need according its number")




#     return selectedMode




# def call_function(selectedMode):
#     if selectedMode == 1:
#         normal_operation_mode()


#     elif selectedMode == 2:
#         maintenance_adjustment_mode()


#     else:
#         data_observation_mode()






# # Here is the main function of selection_of_mode
# def selection_of_mode():
#     while True:
#         try:
#             selectedMode = menu()
#             selectedMode = call_function(selectedMode)


#         except KeyboardInterrupt:
#             selectedMode = menu()

# # password_system()
# maintenance_adjustment_mode()


# placeholder function for push button detecting number of pedestrians
# def pedestrian_presence():
#     numOfPress = 0
#     pushButtonPress = "N"
#     while True:
#         pushButtonPress = input("Is the push button pressed? (Y/N): ")
#         # increase count if push button is pressed
#         if pushButtonPress == "Y":
#             numOfPress += 1
#         else:
#             break
#     # print the number of pedestrians at the beginning of stage 3
#     if stage_three(): 
#         print(f"The number of pedestrians is {numOfPress}.")
#     # resest the number of pedestrians by restarting the function
#     elif stage_one():
#         pedestrian_presence()

def password_system():
    numOfChance = 3
    password = "123456"


    global access


    while numOfChance != 0:
        try:
            userInput = str(input("Please enter the password to access Maintenance Adjustment Mode: "))


            if userInput == password:
                access = True
                break


        except userInput != password:
            numOfChance -= 1
            print(f"""Your password is incorrect
                  Please try again
                  Attempt left {numOfChance}""")


    return access

password_system()