import os
import json
import datetime

class LMS:
    def __init__(self, book_file, library_name ,librarian_pass = "admin123"):
        self.book_file = book_file
        self.library_name = library_name
        self.book_dict = self.load_books()
        self.librarian_pass = librarian_pass

    def load_books(self):
        with open(self.book_file, "r") as bk:
            return json.load(bk)
        

    def save_books(self):
        with open(self.book_file, "w") as bk:
            json.dump(self.book_dict, bk, indent=4)

    def display_book(self):
        print("\n-------------------------- Book List ----------------------------")
        print("ID_NO \t\t Book Title")
        print("-----------------------------------------------------------------")
        for key, value in self.book_dict.items():
            print(f"{key} \t\t {value.get('book_title')} - [{value.get('book_status')}]")

    def issue_book(self):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Id = input("Enter the Book ID: ")
        if Id in self.book_dict.keys():
            if self.book_dict[Id]['book_status']  == "0":
                print(f"Books is already issued ")
            else:
                your_name = input("Enter your name: ")
                self.book_dict[Id]['book_status'] = str(int(self.book_dict[Id]['book_status'])-1)
                self.book_dict[Id]['lender_name'].append(your_name)
                self.book_dict[Id]['issue_date'].append(current_time)
                self.save_books()
                print("Book has been issued successfully.")
        else:
            print("Invalid Book ID. Please try again.")
            self.issue_book()

    def return_book(self):
        Id = input("Enter the Book ID: ")
        if Id in self.book_dict.keys():
            if self.book_dict[Id]['book_status'] == "5":
                print("Book is already available. Please check the Book ID.")
                self.return_book()
            else:
                name = input("Enter your name : ")
                if name in self.book_dict[Id]['lender_name'] :
                    index = self.book_dict[Id]['lender_name'].index(name)
                    self.book_dict[Id]['book_status'] = str(int(self.book_dict[Id]['book_status'])+1)
                    self.book_dict[Id]['lender_name'].pop(index)
                    self.book_dict[Id]['issue_date'].pop(index)
                    self.save_books()
                    print("Book has been returned successfully.")
        else:
            print("Invalid Book ID. Please try again.")
            self.return_book()
        

    def add_book(self):
        confirm = self.librarian_authentication()
        if confirm :
            new_book = input("Enter the Book name: ")
            if new_book == "":
                print("Book name cannot be empty.")
                self.add_book()
            elif len(new_book) > 30:
                print("Book name must be less than 30 characters.")
                self.add_book()
            else:
                next_id = str(int(max(self.book_dict.keys())) + 1) if self.book_dict else "101"
                self.book_dict[next_id] = {
                    "book_title": new_book.strip(),
                    "book_status": "5",
                    "lender_name": [],
                    "issue_date": []
                }
                self.save_books()
                print("Book has been added successfully.")
        else :
            print("Authentication failed")


    def librarian_authentication(self) :
        pas = input("Enter the password : ")
        if pas == self.librarian_pass :
            print("Authentication successful")
            return True
        else : 
            
            return False

    def remove_book (self) :
        confirm = self.librarian_authentication()
        if confirm :
            ID = input("Enter the Book Id : ")
            if ID in self.book_dict.keys() :
                ch = input(f"You are sure to remove '{self.book_dict[ID][ "book_title"]}' then Press 'x' : ")
                if ch == "x" :
                    del self.book_dict[ID]
                    self.save_books()
                    print("Book is removed successfully.")
                else :
                    print("Book is removed not successfully.")
            else :
                print("Check the Book Id")
        else :
            print("Authentication failed")

    def display_librarian(self):
        confirm = self.librarian_authentication()
        if confirm :
            print("\n-------------------------- Book List ----------------------------")
            print("ID_NO \t Book Title")
            print("-----------------------------------------------------------------")
            for key, value in self.book_dict.items():
                print(f"{key} \t {value.get('book_title')} - [{value.get('book_status')}] - [{value.get('lender_name')}] - [{value.get('issue_date')}]")
        else :        
            print("Authentication failed")