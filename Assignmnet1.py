#Program Name: Assignment1.py
#Course: IT3883/Section
#Student Name: Benel Kawata
#Assignment Number: Assignment 1
#Due Date: 09/22/2026
#Purpose: The program aims to display a menu that allows the user to
#         append, clear, or display input  saved in an input buffer as a list. 
#         Additionally, I prefered using abstractions of an array instead of implementing them myself because it is quicker - 
#         although it does not really give me much control over how the code works, it uses tested functions that are tested and reliable.
#Resources: The related course material along with W3Schools, "Python List Methods."
#           https://www.w3schools.com/python/python_lists_methods.asp

#For the purpose of this code, I have decided to use a list for adding data to the input buffer
input_buffer = []
#A while loop will repeat the 4 menu options until the user selects option 4
while True:
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")
    pick = input("Enter your choice (1-4): ")
#Option 1 will append the new string to the list as a separate item
    if pick == "1":
        new = input("Enter your string here: ")
        input_buffer.append(new)
        print("Text appended.\n")
#Option 2 will clear the buffer by removing all entries stored in it
    elif pick == "2":
        if input_buffer:
            input_buffer.clear()
            print("Any data previously entered has been cleared \n")
#This part of the code will let the user know that the buffer is already empty if they attempt to clear it
        else:
            print("No input has been entered yet")
#Option 3 will display each item stored within the buffer as a list.
    elif pick == "3":
        if input_buffer:
            print("\nInput_buffer:")

            for item in input_buffer:
                print(f"- {item}\n") #A formatted string will allow me to insert the variable "item" in the output
        else:
            print("\nThe input buffer is empty or it has been cleared.\n") #It is preceeded and succeeded by \n which acts as a new line escape sequence
#Option 4 will end the loop and exit the program
    elif pick == "4":
        print("Program ended.")
        break
#This part of the code, similarly to the one in option 2, it handles any menu selection outside of the given options
    else:
        print("Invalid choice. Please enter a number from 1 to 4.\n")
