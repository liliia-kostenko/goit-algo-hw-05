from contacts_handler import add_contact, change_contact, show_phone, show_all
from parse_handler import parse_input

def main():
    print("Welcome to the assistant bot!")
    contacts = {}
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            # print("Enter the user name and phone number:")
            # user_input = input("Enter [username] [phone]")
            # args = parse_input(user_input)
            print(add_contact(args, contacts))

        elif command == "change":
            # print("Enter the user name and new phone number:")
            # user_input = input("Enter [username] [new phone]")
            # args = parse_input(user_input)
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
