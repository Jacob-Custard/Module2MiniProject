completed_tasks = ["cook", "mow", "dust"]                                                                                            #creating a list to hold completed tasks    

incomplete_tasks = ["vacuum"]                                                                                                        #creating a list for incomplete tasks


while True:                                                                                                                          #'while' loop so the user can keep cycling through the options for as long as they want
    try:                                                                                                                             #beginingg a 'try' statement to handle invalid user inputs
        print("\nWelcome to the To-Do List App!")                                                                                    #adding a series of print statements to present the user with the options they can select
        print("\n\nMenu:")                                                                                                           
        print("1. Add a task")                                                                                                       
        print("2. View tasks")                                                                                                       
        print("3. Mark a task as complete")                                                                                          
        print("4. Delete a task")                                                                                                    
        print("5. Quit")                                                                                                             
        user_input = int(input("Please enter which operation you'd like to perform (1-5): "))                                        #input statement getting the user's selection so the app can perform the proper task
    except ValueError:                                                                                                               #'except' statement for ValueError in case user entered a string
        print("\nInvalid seleciton please enter a number from 1-5.")                                                                 #print statement letting the user know what happend and what will be accepted
        break                                                                                                                        
    else:                                                                                                                            
        print("\nThank you for your selection")                                                                                      
    finally:                                                                                                                         
        print("\nThank you for opening the To-Do List app.\n")                                                                                                                                                                                             
                                                                                                                                     
    if user_input == 1:                                                                                                              #start of a series of 'if', 'elif' statements determining what to do based off the user input
        new_task = input("Enter your new task:\n ")                                                                                  #asking the user for the task they'd like to add and appending it to the incomplete tasks list
        incomplete_tasks.append(new_task)                                                                                            
        print(f"{new_task} has been added to the incomplete tasks list.")                                                                               
                                                                                                                                     
    elif user_input == 2:                                                                                                            
        for task in completed_tasks:                                                                                                 
            print(task + ": completed")                                                                                              #print statements that will print off the current tasks for both the complete and incomplete lists
        for task in incomplete_tasks:                                                                                                
            print( task + ": incomplete")                                                                                            #print statement formatted to give the user 'task: complete/incomplete' so they know which list each task is in                                                                              
                                                                                                                                     
    elif user_input == 3:                                                                                                            
        print(f"This is the current list of incomplete tasks:\n{incomplete_tasks}")                                                  #print statement telling the user what the current list of incomplete tasks is
        try:                                                                                                                         
            finish_task = input("Which task would you like to mark as complete?: ")                                                  #input asking which task the user would like to set as complete
            incomplete_tasks.remove(finish_task)                                                                                     #removing the selected task from the incomplete list
            completed_tasks.append(finish_task)                                                                                      #appending the task to the complete tasks list
            print(f"\nThe task {finish_task} has been marked as completed")                                                          #print statement letting the user know the selected task has been marked as compelete
        except ValueError:                                                                                                           #'except' statement for ValueError in case of an invalid entry
            print("\nThe task entered either doesnt exist or was entered incorrectly.")                                              #print statement letting the user know what happened

    elif user_input == 4:                                                                                                            
        select_list = input("Which task list do you wish to delete from? (complete/incomplete): ").lower()                           #input asking the user which list they'd like to delete from
        if select_list == "complete":                                                                                                #'if', 'elif' statement determing the user's choice
            try:                                                                                                     
                print(f"This is the current completed tasks list:\n{completed_tasks}")                                               #print statement telling the user the current list of tasks                        
                remove_task = input("Which task would you like to remove?: ")                                                        #input asking the user which task should be removed                           
                completed_tasks.remove(remove_task)                                                                                  #removing the selected task from the selected list
                print(f"\n{remove_task} has been removed from the completed tasks list.")                                            #print statement to tell the user the selected task has been removed from the selected list
            except ValueError:                                                                                                       
                print("\nThe task entered either doesnt exist or was entered incorrectly.")                                          
                                         
        elif select_list == "incomplete":                                                                                            
            try:                                                                                                                     #starting a 'try' statement to help with user input error
                print(f"This is the current incomplete tasks list:\n{incomplete_tasks}")                                             
                remove_task = input("Which task would yo like to remove?: ")                                                         
                incomplete_tasks.remove(remove_task)                                                                                 
                print(f"\n{remove_task} has been removed from the incomplete tasks list.")                                           
            except ValueError:                                                                                                       #'except' statement for ValueError in case of user an unsupported user input
                print("\nThe task entered either doesn't exist or was entered incorrectly.")                                         #print statement letting the user know their input wasn't recognized
                                                                                                                                     
        else:                                                                                                                        #else statement in case the user enters something not recognized by the 'if' loop
            print("Invalid entry please enter either complete or incomplete.")                                                       #print statement letting the user know their entry wasn't recognized 
                                                                                                                                     
    elif user_input == 5:                                                                                                            
        sure_quit = input("Are you sure you'd like to quit the application? (yes/no): ").lower()                                     #designating an input as a new variable and asking the user if they would like to quit, added .lower() in case the user capitalized a letter
        if sure_quit != "no":                                                                                                        # determining if the users input was 'no' 
            break                                                                                                                    # break statement ending the while loop
    else:                                                                                                                            
        print("\nUnknown selection made. Please enter the corresponding number (1-5) to the operation you'd like to perform.")       #print statement letting the user know they entered an unrecognized number



