from tasks import Tasks
from accounts import Accounts

accounts = Accounts()

options = '''--=> Welcome to My TODO App <=--
            Please make a selection
            1. Login to My Account
            2. Register With Us
            0. Exit
        '''

main_menu = '''      --=> Welcome to My TODO App <=--
            Please make a selection
            1. Create TODO List
            2. Delete item from TODO List
            3. Delete All Items in TODO List
            4. Mark Item in TODO List as Finished
            5. Logout
            0. Exit
            '''

def main():
    print(f"{options}")
    option = input("Selection: ")
    check_menu_option(option)
    
def menu():
    print(f"{main_menu}")
    menu_item = input("Selection: ")
    menu_selection(menu_item)

def menu_selection(opt):
    if opt == "":
        print("Please enter a valid option!")
        return menu()
    if opt == '1':
        return create_todo()
    if opt == '2':
        return "Option 2"
    if opt == '3':
        return "Option 3"
    if opt == '4':
        return "Option 4"
    if opt == '5':
        return main()
    if opt == '0':
        exit()
    else:
        print("Kindly enter a valid option!")
        return menu()

def check_menu_option(value):
    if value == "":
        print("Please enter a valid option!")
        return main()
    if value == '1':
        return login_prompt()
    if value == '2':
        return signup_prompt()
    if value == '0':
        exit()
    else:
        print("Kindly enter a valid option!")
        return main()

def signup_prompt():
    print("--=> My TODO Sign Up <=--")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == "" and password == "":
        print("Please enter reqiured values")
        signup_prompt()
    elif accounts.create_account(username, password) == "Account created":
        login_prompt()
    else:
        signup_prompt()

def login_prompt():
    print(accounts.accounts_list)
    print("--=> My TODO Login <=--")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == "" and password == "":
        print("Please enter reqiured values")
        login_prompt()
    elif accounts.account_existance(username, password) == "User exists":
        menu()
    else:
        print("Do you really have an account with us!?")
        login_prompt()

def create_todo():
    title = input("Title: ")
    descr = input("Description: ")
    if title == "":
        print("Please enter valid data")
        create_todo()
    if todo_existance(title) == True:
        print("ToDo List Already exists!")
        create_todo()
    if Tasks().create_task(title, descr) == "created":
        print("ToDo List Created Successfully")
        print(Tasks().todo_list)
        print(Tasks().descriptions)
        Tasks().add_task_item(title)
        if Tasks().add_task_item(title) == "done":
            menu()

def add_or_remove():
    print("Add or remove items from")
    print(Tasks().todo_list_items)
    

def todo_existance(title):
    for items in Tasks().todo_list:
        if title in items:
            return True
        else:
            return False

if __name__ == "__main__":
    main()