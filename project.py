from main1 import LMS 

try:
    l = LMS("books1.json", "HAMMAD'S Library")

    press_key_dict = {
        "q": "Quit",
        "d": "Display books",
        "i": "Issue book",
        "a": "Add book",
        "r": "Return book",
        "x": "Remove book",
        "f": "Full information"
    }

    press_key = ""
    while press_key != "q":
        print("\n-------------------- Welcome to Hammad's Library Management System -------------------")
        print('''
    Press the following keys:
    d : Display books
    i : Issue a book
    r : Return a book
    a : Add a book (Librarian only)
    x : Remove a book (Librarian only)
    f : Full information (Librarian only)
    q : Quit the program
        ''')
        press_key = input("Enter your choice: ").lower()

        if press_key == "d":
            print("You selected: Display books")
            l.display_book()
        elif press_key == "f":
            print("You selected: Full information")
            l.display_librarian()
        elif press_key == "i":
            print("You selected: Issue book")
            l.issue_book()
        elif press_key == "a":
            print("You selected: Add book")
            l.add_book()
        elif press_key == "r":
            print("You selected: Return book")
            l.return_book()
        elif press_key == "x":
            print("You selected: Remove  book")
            l.remove_book()   
        elif press_key == "q":
            print("Thank you for using the Library Management System. Goodbye!")
        else:
            print("Invalid input. Please try again.")

except Exception as e:
    print("Something went wrong:", e)
