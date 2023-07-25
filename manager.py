def read_entries(filename):
    try:
        with open(filename, "r") as file:
            entries = [line.strip().split(", ") for line in file]
        print("Entries read successfully!")
        return entries
    except FileNotFoundError:
        print("File not found.")
        return []

def save_entries(entries, filename):
    try:
        with open(filename, "w") as file:
            for entry in entries:
                file.write(", ".join(entry) + "\n")
        print("Entries saved successfully!")
    except:
        print("Error occurred while saving entries.")

def add_entry(entries, entry, reply_message):
    first_name, email, phone_number, address = entries

    if any(e[1] == email for e in entries):
        print("Email already exists. Entry not added.")
        return

    entries.append(entries)
    entries.sort(key=lambda x: x[0])
    print("Entry added successfully.")
    print(reply_message)  # Print the reply message

def remove_entry(entries, email):
    for entry in entries:
        if entry[1] == email:
            entries.remove(entry)
            print("Entry removed successfully.")
            return

    print("Entry not found.")

def update_entry(entries, entry):
    email = entry[1]

    for i, e in enumerate(entries):
        if e[1] == email:
            entries[i] = entry
            entries.sort(key=lambda x: x[0])
            print("Entry updated successfully.")
            return

    print("Entry not found.")

def search_entries(entries, keyword):
    found_entries = []

    for entry in entries:
        if any(keyword.lower() in field.lower() for field in entry):
            found_entries.append(entry)

    if found_entries:
        print("Matching entries:")
        for entry in found_entries:
            print(", ".join(entry))
    else:
        print("No matching entries found.")

def print_entries(entries):
    if entries:
        print("All entries:")
        for entry in entries:
            print(", ".join(entry))
    else:
        print("No entries found.")

def validate_email(email):
    if "@" not in email or "." not in email:
        return False
    return True

def handle_input(entries, input_str):
    args = input_str.split()
    action = args[0].lower()

    if action == "read":
        if len(args) != 2:
            print("Invalid number of arguments for 'read' action.")
            return entries
        filename = args[1]
        return read_entries(filename)
    elif action == "save":
        if len(args) != 2:
            print("Invalid number of arguments for 'save' action.")
            return entries
        filename = args[1]
        save_entries(entries, filename)
        return entries
    elif action == "add":
        if len(args) != 2:
            print("Invalid number of arguments for 'add' action.")
            return entries
        entry_fields = args[1].split(",")
        if len(entry_fields) != 4:
            print("Invalid number of fields for 'add' action.")
            return entries
        entry = [field.strip() for field in entry_fields]
        if not validate_email(entry[1]):
            print("Invalid email address.")
            return entries

        reply_message = "Thank you for adding the entry. Your request has been received."
        add_entry(entries, entry, reply_message)
        return entries
    elif action == "remove":
        if len(args) != 2:
            print("Invalid number of arguments for 'remove' action.")
            return entries
        email = args[1]
        remove_entry(entries, email)
        return entries
    elif action == "update":
        if len(args) != 6:
            print("Invalid number of arguments for 'update' action.")
            return entries
        entry = args[1:]
        if not validate_email(entry[1]):
            print("Invalid email address.")
            return entries
        update_entry(entries, entry)
        return entries
    elif action == "search":
        if len(args) != 2:
            print("Invalid number of arguments for 'search' action.")
            return entries
        keyword = args[1]
        search_entries(entries, keyword)
        return entries
    elif action == "print":
        print_entries(entries)
        return entries
    else:
        print("Invalid action keyword.")
        return entries

def main():
    entries = []
    while True:
        input_str = input("Enter an action keyword followed by the required input: ")
        if input_str.lower() == "quit":
            break
        entries = handle_input(entries, input_str)

if __name__ == "__main__":
    main()
