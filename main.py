#Group 16
# Michael Sena
# Andrew Arroyos
# Lab Assignment 6- This program will make a roledex that allows the user to view, search, modify
# a contact list made of contact objects (using operator overloading)

from contact import Contact
import check_input

def read_file():
    """
    Reads contacts from addresses.txt

    Returns:
        list: the sorted list of actual Contact objects 
    """

    #creates an empty list for the Contact objects 
    contacts = []

    #opens the file and reads each contact
    with open("addresses.txt", "r") as file:
        for line in file:

            #removes the newline and seperate the contact info
            data = line.strip().split(",")
            
            #create a Contact object using the data from the file
            contact = Contact(data[0], data[1], data[2], data[3], data[4], data[5])

            #add the contact object to the list
            contacts.append(contact)
    
    #sort contacts by last name, then first name
    contacts.sort()

    return contacts

def write_file(contacts):
    """
    Writes all contacts back to addresses.txt 

    Args:
        contacts (list): a list of Contact objects
    """

    #open the file in write mode to overwrite the old contents
    with open("addresses.txt", "w") as file: 

        #write each contact to the file using its repr format
        for contact in contacts:
            file.write(repr(contact) + "\n")

def get_menu_choice():
    """ 
    Displays the main menu and returns the user's valid choice
    
    Returns:
        int: menu choice from 1 through 5
    """

    #display the main rolodex menu
    print("Rolodex Menu:")
    print("1. Display Contacts")
    print("2. Add Contact")
    print("3. Search Contacts")
    print("4. Modify Contact")
    print("5. Save and Quit")

    #returns a validated menu choice
    return check_input.get_int_range("> ", 1, 5)

def modify_contact(cont):
    """
    Allows the user to modify a Contact's objects information

    Args:
        cont (Contact): contact that we want to modify 
    """
    choice = 0

    #keeps displaying the modify menu until the user choosees Save
    while choice != 7:
        print("Modify Menu:")
        print("1. First name")
        print("2. Last name")
        print("3. Phone")
        print("4. Address")
        print("5. City")
        print("6. Zip")
        print("7. Save")

        #get a validated modify menu choice
        choice = check_input.get_int_range("> ", 1, 7)

        #update the selected Contact attribute
        if choice == 1:
            cont.first_name = input("Enter first name: ")
        elif choice == 2:
            cont.last_name = input("Enter last name: ")
        elif choice == 3:
            cont.phone = input("Enter phone #: ")
        elif choice == 4:
            cont.address = input("Enter address: ")
        elif choice == 5:
            cont.city = input("Enter city: ")
        elif choice == 6:
            cont.zip = input("Enter zip: ")

def main():
    """
    Runs the Rolodex contact program
    """

    #read the contacts from the file when the program begins
    contacts = read_file()

    choice = 0

    #continue displaying the menu until the user chooses Save and Quit
    while choice != 5:
        choice = get_menu_choice()

        #display all contacts
        if choice == 1:
            print(f"Number of contacts: {len(contacts)}")

            number = 1
            #number and display each contact in sorted order 
            for contact in contacts:
                print(f"{number}. {str(contact)}")
                number += 1

        #add a new contact
        elif choice == 2:
            print("Enter new contact:")

            #get the information for the new contact
            first_name = input("First name: ")
            last_name = input("Last name: ")
            phone = input("Phone #: ")
            address = input("Address: ")
            city = input("City: ")
            zip_code = input("Zip: ")

            #create a new contact object
            contact = Contact(first_name,last_name,phone,address,city,zip_code)

            #add the new contact and resort the list
            contacts.append(contact)
            contacts.sort()

        #search for contacts
        elif choice == 3:
            print("Search: ")
            print("1. Search by last name")
            print("2. Search by zip")

            # get a validated search option
            search_choice = check_input.get_int_range("> ", 1, 2)

            #search for all contacts with the entered last name
            if search_choice ==1:
                search_data = input("Enter last name: ")

                for contact in contacts:
                    if contact.last_name == search_data:
                        print(str(contact))
            
            #search for all contacts with the entereed zip cod
            else:
                search_data = input("Enter zip code: ")

                for contact in contacts:
                    if contact.zip == search_data:
                        print(str(contact))

        #modify an existing contact
        elif choice == 4:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            #start with no matching contact found
            found_contact = None

            #search for a contact with bot hthe matching first and last name
            for contact in contacts:
                if(contact.first_name == first_name and contact.last_name == last_name):
                    found_contact = contact
                    break

            #only display the modify menu if the contact was found
            if found_contact is not None:
                print(str(found_contact))
                modify_contact(found_contact)

                #name may have changed so re sort the list
                contacts.sort()
            else:
                print("Contact not found.")

        # save contacts and quit the program 
        elif choice == 5:
            print("Saving File...")

            #overwrite the file with the current contact list
            write_file(contacts)
            print("Ending Program")
main()
        
