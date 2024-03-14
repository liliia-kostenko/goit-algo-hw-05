def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            if isinstance(e, KeyError):
                return "Enter correct user name. This contact is not in the database."
            elif isinstance(e, ValueError):
                return "Give me name and phone please."
            elif isinstance(e, IndexError):
                return "Enter the argument for the command."
    return inner

def validate_input(func):
    def wrapper(args, contacts):
        name, phone = args
        if not name.isalpha():
            return "Name must contain only letters."
        if not phone.isdigit():
            return "Phone number must contain only digits."
        return func(args, contacts)
    return wrapper

def check_empty_dict(func):
    def wrapper(contacts):
        if len(contacts) == 0:
            return ValueError("Dictionary is empty.")
        return func(contacts)
    return wrapper


@validate_input
@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@validate_input
@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."

@validate_input
@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name not in contacts:
        raise KeyError
    return contacts[name]
    
@check_empty_dict
def show_all(contacts):
    all_contacts = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return all_contacts
