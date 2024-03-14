def parse_input(user_input):
    command, *args = user_input.strip().split()
    command = command.lower()
    return command, args