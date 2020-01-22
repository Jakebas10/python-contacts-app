from contact import Contact
from db_conn import getContacts, addContact

def main():

    showMenu()
    option = int(input("What do you want to do? "))

    while option != 3:
        if option == 1:
            getContacts()
        elif option == 2:
            addContact()

        showMenu()
        option = int(input("What do you want to do? "))

    print("Bye")

def showMenu():
    print("Contacts App")
    print("1) Show Contacts")
    print("2) Add Contact")
    print("3) Exit")

if __name__ == '__main__':
    main()