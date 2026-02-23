from datetime import datetime, timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent          # /src
DATA_DIR = BASE_DIR.parent / "data"                # /data

def data_file(name: str) -> Path:
    return DATA_DIR / name


stored_a = "mok"
stored_b = "123"

print("Welcome to Brickfields Kuala Lumpur Community Library System")
print("=============================================================")

login_user = None  # will store current member info after login


def choose_char():
    x = input("1. Admin\n2. Librarian\n3. Member\n4. Exit\nPlease select your role: ")

    if x == "1":
        login_admin()
        choose_admin_role()
    elif x == "2":
        login_lib()
        main_menu_lib()
    elif x == "3":
        login_mem()
        main_menu_mem()
    elif x == "4":
        print("Exit successfully.")
        exit()
    else:
        print("Please enter a valid number from 1 to 4!\n")
        return choose_char()


def login_admin():
    print("\nSystem Admin Account")
    print("====================")
    while True:
        c = input("Enter username: ").strip()
        d = input("Enter password: ").strip()

        if c == stored_a and d == stored_b:
            print("Login successfully.")
            return
        print("Invalid username or password. Please enter again!\n")


def logout_admin():
    print("\nSystem Admin Logout")
    print("====================")
    while True:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        if username == stored_a and password == stored_b:
            print("Logout successfully.")
            exit()
        else:
            print("Invalid username or password. Please enter again!\n")


def mem_list():
    members_list = []
    with open(data_file("member_info.txt"), "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                items = line.strip().split(";")
                if len(items) == 3:
                    members_list.append(
                        {"userID": items[0], "username": items[1], "password": items[2]}
                    )
    return members_list


def librarian_list():
    libs = []
    with open(data_file("librarian_info.txt"), "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                items = line.strip().split(";")
                if len(items) == 2:
                    libs.append({"username": items[0], "password": items[1]})
    return libs


def book_list():
    books = []
    with open(data_file("bookCatalogues.txt"), "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                items = line.strip().split(";")
                if len(items) >= 4:
                    books.append(
                        {"bookID": items[0], "title": items[1], "author": items[2], "status": items[3]}
                    )
    return books


def resetList2():
    mylist3 = []
    with open(data_file("loanedBook.txt"), "r", encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue
            items = line.strip().split(";")
            if len(items) == 4:
                due_date = datetime.strptime(items[2], "%Y-%m-%d").date()
                mylist3.append(
                    {
                        "userID": items[0],
                        "bookID": items[1],
                        "DueDate": due_date,
                        "OverdueFee(RM)": items[3].strip(),
                    }
                )
    return mylist3


def goBackMenu_admin_lib():
    goBack = input("Go back to main menu(Y/N): ").lower()
    if goBack == "y":
        choose_admin_lib()
    elif goBack == "n":
        logout_admin()
    else:
        return goBackMenu_admin_lib()


def goBackMenu_admin_mem():
    goBack = input("Go back to main menu(Y/N): ").lower()
    if goBack == "y":
        choose_admin_mem()
    elif goBack == "n":
        logout_admin()
    else:
        return goBackMenu_admin_mem()


def choose_admin_role():
    print("\nChoose Role")
    print("=============")
    choose_role = input("Which role you want to operate(1.librarian / 2.member): ")

    if choose_role == "1":
        choose_admin_lib()
    elif choose_role == "2":
        choose_admin_mem()
    else:
        print("Please enter again!")
        return choose_admin_role()


def choose_admin_lib():
    print("\nSystem Admin Main Menu (Librarian)")
    print("==================================")
    print("1. Add librarian")
    print("2. View librarian")
    print("3. Search librarian")
    print("4. Edit librarian")
    print("5. Remove librarian")
    print("6. Log out")
    choose = input("Enter a number to choose: ")
    if choose == "1":
        add_lib()
    elif choose == "2":
        view_lib()
    elif choose == "3":
        search_lib()
    elif choose == "4":
        edit_lib()
    elif choose == "5":
        remove_lib()
    elif choose == "6":
        logout_admin()
    else:
        print("Please enter a valid number from 1 to 6!")
        return choose_admin_lib()

    goBackMenu_admin_lib()


def choose_admin_mem():
    print("\nSystem Admin Main Menu (Member)")
    print("===============================")
    print("1. Add member")
    print("2. View member")
    print("3. Search member")
    print("4. Edit member")
    print("5. Remove member")
    print("6. Log out")
    choose = input("Enter a number to choose: ")

    if choose == "1":
        add_member()
    elif choose == "2":
        view_member()
    elif choose == "3":
        search_member()
    elif choose == "4":
        edit_member()
    elif choose == "5":
        remove_member()
    elif choose == "6":
        logout_admin()
    else:
        print("Please enter a valid number from 1 to 6!")
        return choose_admin_mem()

    goBackMenu_admin_mem()


def add_lib():
    print("\nAdd new librarian")
    print("=================")
    name = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if not name or not password:
        print("Username and password cannot be empty. Please enter again.\n")
        return add_lib()

    with open(data_file("librarian_info.txt"), "a", encoding="utf-8") as file:
        file.write(f"{name};{password}\n")
    print("New librarian added successfully.")


def view_lib():
    new_list = librarian_list()
    print("\nView librarian")
    print("===============")
    no = 1
    for lib in new_list:
        print(f"{no}. Username: {lib['username']}, Password: {lib['password']}")
        no += 1


def search_lib():
    print("\nSearch librarian")
    print("================")
    search = input("Enter the name to search (or enter EXIT): ")

    if search.upper() == "EXIT":
        return

    newlist = librarian_list()
    for lib in newlist:
        if lib["username"].lower() == search.lower():
            print(f"Username: {lib['username']}, Password: {lib['password']}")
            return
    print("Librarian Not Found!")
    return search_lib()


def edit_lib():
    print("\nEdit librarian")
    print("==============")
    newlist = librarian_list()
    no = 1
    for i in newlist:
        print(f"{no}. Username: {i['username']}, Password: {i['password']}")
        no += 1

    input_name = input("Enter the username to edit (or enter EXIT): ")

    if input_name.upper() == "EXIT":
        return

    for lib in newlist:
        if lib["username"].lower() == input_name.lower():
            print(f"\nEditing Username: {lib['username']}, Password: {lib['password']}")

            new_name = input("Enter new username (or press Enter to keep the current username): ").strip()
            new_password = input("Enter new password (or press Enter to keep the current password): ").strip()

            if new_name:
                lib["username"] = new_name
            if new_password:
                lib["password"] = new_password

            with open(data_file("librarian_info.txt"), "w", encoding="utf-8") as file:
                for row in newlist:
                    file.write(f"{row['username']};{row['password']}\n")

            print("\nLibrarian information updated! Here is the updated information:")
            print("================================================================")
            print(f"Username: {lib['username']}, Password: {lib['password']}\n")
            return

    print("Librarian Not Found!")
    return edit_lib()


def remove_lib():
    print("\nRemove librarian")
    print("================")
    newlist = librarian_list()
    no = 1
    for i in newlist:
        print(f"{no}. Username: {i['username']}, Password: {i['password']}")
        no += 1

    input_name = input("Enter the username to remove (or enter EXIT): ")

    if input_name.upper() == "EXIT":
        return

    for index, lib in enumerate(newlist):
        if lib["username"].lower() == input_name.lower():
            newlist.pop(index)
            print("Librarian removed successfully.")
            break
    else:
        print("Librarian Not Found!")
        return remove_lib()

    with open(data_file("librarian_info.txt"), "w", encoding="utf-8") as file:
        for lib in newlist:
            file.write(f"{lib['username']};{lib['password']}\n")


def add_member():
    print("\nAdd new member")
    print("==============")
    v = input("Enter userID: ").upper().strip()
    x = input("Enter username: ").strip()
    y = input("Enter password: ").strip()

    if not v or not x or not y:
        print("Username and password cannot be empty.\n")
        return add_member()

    with open(data_file("member_info.txt"), "a", encoding="utf-8") as file:
        file.write(f"{v};{x};{y}\n")
    print("New member added successfully.")


def view_member():
    new_list = mem_list()
    print("\nView member")
    print("===========")
    no = 1
    for member in new_list:
        print(f"{no}. UserID: {member['userID']}, Username: {member['username']}, Password: {member['password']}")
        no += 1


def search_member():
    print("\nSearch member")
    print("=============")
    search = input("Enter the userID to search (or enter EXIT): ")

    if search.upper() == "EXIT":
        return

    newlist = mem_list()
    for member in newlist:
        if member["userID"].lower() == search.lower():
            print(f"UserID: {member['userID']}, Username: {member['username']}, Password: {member['password']}")
            return
    print("Member Not Found!")
    return search_member()


def edit_member():
    print("\nEdit member")
    print("===========")
    newlist = mem_list()
    no = 1
    for i in newlist:
        print(f"{no}. UserID: {i['userID']}, Username: {i['username']}, Password: {i['password']}")
        no += 1

    inputID = input("Enter the userID to edit (or enter EXIT): ")

    if inputID.upper() == "EXIT":
        return

    for member in newlist:
        if member["userID"].lower() == inputID.lower():
            print(f"\nEditing UserID: {member['userID']}, Username: {member['username']}, Password: {member['password']}")

            new_userID = input("Enter new userID (or press Enter to keep the current userID): ").upper().strip()
            new_name = input("Enter new username (or press Enter to keep the current username): ").strip()
            new_password = input("Enter new password (or press Enter to keep the current password): ").strip()

            if new_userID:
                member["userID"] = new_userID
            if new_name:
                member["username"] = new_name
            if new_password:
                member["password"] = new_password

            with open(data_file("member_info.txt"), "w", encoding="utf-8") as file:
                for row in newlist:
                    file.write(f"{row['userID']};{row['username']};{row['password']}\n")

            print("\nMember information updated! Here is the updated information:")
            print("=============================================================")
            print(f"UserID: {member['userID']}, Username: {member['username']}, Password: {member['password']}\n")
            return

    print("Member Not Found!")
    return edit_member()


def remove_member():
    print("\nRemove member")
    print("=============")
    newlist = mem_list()
    no = 1
    for i in newlist:
        print(f"{no}. UserID: {i['userID']}, Username: {i['username']}, Password: {i['password']}")
        no += 1

    input_ID = input("Enter the userID to remove (or enter EXIT): ")

    if input_ID.upper() == "EXIT":
        return

    for index, member in enumerate(newlist):
        if member["userID"].lower() == input_ID.lower():
            newlist.pop(index)
            print("Member removed successfully.")
            break
    else:
        print("Member Not Found!")
        return remove_member()

    with open(data_file("member_info.txt"), "w", encoding="utf-8") as file:
        for member in newlist:
            file.write(f"{member['userID']};{member['username']};{member['password']}\n")


def login_lib():
    librarians = librarian_list()
    print("\nLibrarian Account")
    print("=================")

    while True:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        for lib in librarians:
            if lib["username"] == username and lib["password"] == password:
                print("Login successfully.")
                return
        print("Invalid username or password. Please enter again!\n")


def goBackMenu_lib():
    goBack = input("Go to back to main menu(Y/N): ").lower()
    if goBack == "y":
        main_menu_lib()
    elif goBack == "n":
        print("Exit System Successfully.")
        exit()
    else:
        return goBackMenu_lib()


def main_menu_lib():
    print("\nLibrarian Main Menu")
    print("===================")
    print("1. Add new book into the catalogue")
    print("2. View all existing book catalogue")
    print("3. Search book from the catalogue")
    print("4. Edit book information")
    print("5. Remove book from catalogue")
    print("6. View Book Loan")
    print("7. Log out")
    choose = input("Enter a number to choose: ")

    if choose == "1":
        add_book()
    elif choose == "2":
        view_book()
    elif choose == "3":
        search_book()
    elif choose == "4":
        edit_book()
    elif choose == "5":
        remove_book()
    elif choose == "6":
        book_loan()
    elif choose == "7":
        print("Exit System Successfully.")
        exit()
    else:
        print("Please enter a valid number from 1 to 7!")
        return main_menu_lib()

    goBackMenu_lib()


def add_book():
    print("\nAdd new book")
    print("=============")
    bookID = input("Enter bookID: ").upper().strip()
    title = input("Enter name: ").title().strip()
    author = input("Enter author: ").title().strip()
    status = input("Enter status (available/unavailable): ").strip().lower()

    if not bookID or not title or not author or not status:
        print("BookID, title, author and status cannot be empty.\n")
        return add_book()

    with open(data_file("bookCatalogues.txt"), "a", encoding="utf-8") as file:
        file.write(f"{bookID};{title};{author};{status}\n")

    print("New book added successfully.")


def view_book():
    print("\nBook Catalogues")
    print("===============")
    mylist = book_list()

    no = 1
    for book in mylist:
        print(f"{no}. BookID: {book['bookID']}, Title: {book['title']}, Author: {book['author']}, Status: {book['status']}")
        no += 1


def search_book():
    print("\nSearch book catalogues")
    print("======================")
    mylist = book_list()
    no = 1
    for book in mylist:
        print(f"{no}. BookID: {book['bookID']}")
        no += 1

    search = input("Enter the bookID to search: ").upper().strip()

    for book in mylist:
        if book["bookID"].upper() == search:
            print(f"BookID: {book['bookID']}, Title: {book['title']}, Author: {book['author']}, Status: {book['status']}")
            return

    print("Book Not Found!")
    return search_book()


def edit_book():
    print("\nEdit book")
    print("=========")
    mylist = book_list()
    no = 1
    for i in mylist:
        print(f"{no}. BookID: {i['bookID']}, Title: {i['title']}, Author: {i['author']}, Status: {i['status']}")
        no += 1

    inputItem2 = input("Enter the BookID to edit (or enter EXIT): ").upper().strip()
    if inputItem2 == "EXIT":
        return

    for book in mylist:
        if book["bookID"].upper() == inputItem2:
            print(f"\nEditing BookID: {book['bookID']}, Title: {book['title']}, Author: {book['author']}, Status: {book['status']}")

            newBookTitle = input("Enter new title (or press Enter to keep the current title): ").title().strip()
            newAuthor = input("Enter new author (or press Enter to keep the current author): ").title().strip()
            newStatus = input("Enter new status (available/unavailable) (or press Enter to keep the current status): ").strip().lower()

            if newBookTitle:
                book["title"] = newBookTitle
            if newAuthor:
                book["author"] = newAuthor
            if newStatus:
                book["status"] = newStatus

            with open(data_file("bookCatalogues.txt"), "w", encoding="utf-8") as file:
                for row in mylist:
                    file.write(f"{row['bookID']};{row['title']};{row['author']};{row['status']}\n")

            print("\nBook information updated! Here is the updated information:")
            print("=============================================================")
            print(f"BookID: {book['bookID']}, Title: {book['title']}, Author: {book['author']}, Status: {book['status']}\n")
            return

    print("Book Not Found!")
    return edit_book()


def remove_book():
    print("\nRemove book")
    print("============")
    mylist = book_list()
    no = 1
    for i in mylist:
        print(f"{no}. BookID: {i['bookID']}, Title: {i['title']}, Author: {i['author']}, Status: {i['status']}")
        no += 1

    inputItem = input("\nEnter the bookID to remove (or enter EXIT): ").upper().strip()
    if inputItem == "EXIT":
        return

    for index, data in enumerate(mylist):
        if data["bookID"].upper() == inputItem:
            mylist.pop(index)
            print("Book removed successfully.")
            break
    else:
        print("Book Not Found!")
        return remove_book()

    with open(data_file("bookCatalogues.txt"), "w", encoding="utf-8") as file:
        for row in mylist:
            file.write(f"{row['bookID']};{row['title']};{row['author']};{row['status']}\n")


def book_loan():
    print("\nBook Loan Process")
    print("=================")
    print("Enter UserID and BookID to loan a book.")
    userID = input("Enter UserID: ").upper().strip()

    bookloan_list = resetList2()
    bookCat_list = book_list()
    user_list = mem_list()

    bookID = input("Enter BookID: ").upper().strip()
    currDate = datetime.today().date()
    dueDate = (currDate + timedelta(days=14))
    dueDate_str = dueDate.strftime("%Y-%m-%d")
    overdue_fee = 0

    user_exists = any(u["userID"].upper() == userID for u in user_list)
    if not user_exists:
        print(f"UserID {userID} does not exist. Please try again.")
        return

    book_exists = any(b["bookID"].upper() == bookID for b in bookCat_list)
    if not book_exists:
        print(f"BookID {bookID} does not exist. Please try again.")
        return

    for loan in bookloan_list:
        if loan["bookID"].upper() == bookID:
            print(f"Sorry, Book {bookID} is already loaned to another member.")
            return

    loan_count = sum(1 for loan in bookloan_list if loan["userID"].upper() == userID)
    if loan_count >= 5:
        print("This user has loaned the maximum number of 5 books.")
        return

    # Check overdue (block borrowing if overdue exists)
    for loan in bookloan_list:
        if loan["userID"].upper() == userID:
            date_diff = (currDate - loan["DueDate"]).days
            if date_diff > 0:
                print("You have overdue books and not allow to borrow new books.")
                return

    # Update book status
    for book in bookCat_list:
        if book["bookID"].upper() == bookID:
            book["status"] = "unavailable"
            break

    with open(data_file("bookCatalogues.txt"), "w", encoding="utf-8") as file:
        for book in bookCat_list:
            file.write(f"{book['bookID']};{book['title']};{book['author']};{book['status']}\n")

    with open(data_file("loanedBook.txt"), "a", encoding="utf-8") as file:
        file.write(f"{userID};{bookID};{dueDate_str};{overdue_fee}\n")

    print(f"Book {bookID} has been loaned successfully to {userID}. Due date is {dueDate_str}.")


def login_mem():
    global login_user
    print("\nLibrary Member Account")
    print("======================")
    members = mem_list()

    while True:
        input_username = input("Enter username: ").strip()
        input_password = input("Enter password: ").strip()

        for member in members:
            if input_username == member["username"] and input_password == member["password"]:
                print("Login successfully.")
                login_user = member
                return
        print("Invalid username or password. Please enter again!\n")


def main_menu_mem():
    print("\nLibrary Member Main Menu")
    print("========================")
    print("1. View current loaned book")
    print("2. Update profile information")
    print("3. Search book catalogues")
    print("4. Log out")
    choice = input("Enter a number to choose: ")

    if choice == "1":
        view_loanbook()
    elif choice == "2":
        update_profile()
    elif choice == "3":
        search_bookCat()
    elif choice == "4":
        print("Exit System Successfully.")
        exit()
    else:
        print("Please enter a valid number from 1 to 4!")
        return main_menu_mem()

    goBackMenu_mem()


def goBackMenu_mem():
    goBack = input("Go to back to main menu(Y/N): ").lower()
    if goBack == "y":
        main_menu_mem()
    elif goBack == "n":
        print("Exit System Successfully.")
        exit()
    else:
        return goBackMenu_mem()


def view_loanbook():
    global login_user
    print("\nYour current loaned book")
    print("========================")
    loaned_books = resetList2()
    bookCat = book_list()

    found = False
    for loan in loaned_books:
        if loan["userID"].upper() == login_user["userID"].upper():
            print(
                f"BookID: {loan['bookID']}, DueDate: {loan['DueDate']}, OverdueFee: RM {loan['OverdueFee(RM)']}"
            )
            found = True

    if not found:
        print("No books are currently loaned.")
        return

    return_book = input("Do you want to return the book(s) and pay the overdue fee?(y/n): ").strip().lower()
    if return_book != "y":
        print("Please return before the due date!")
        return

    books_to_return = input("Enter the BookID of the book(s) want to return (seperated by ,): ").strip().split(",")
    return_ids = [b.strip().upper() for b in books_to_return if b.strip()]

    # remove loans
    new_loans = []
    for loan in loaned_books:
        if loan["userID"].upper() == login_user["userID"].upper() and loan["bookID"].upper() in return_ids:
            continue
        new_loans.append(loan)

    # write back loans (format DueDate)
    with open(data_file("loanedBook.txt"), "w", encoding="utf-8") as file:
        for loan in new_loans:
            due_str = loan["DueDate"].strftime("%Y-%m-%d")
            file.write(f"{loan['userID']};{loan['bookID']};{due_str};{loan['OverdueFee(RM)']}\n")

    print("Selected books have been successfully returned.")

    # update book status: available if not currently loaned
    still_loaned_bookids = {loan["bookID"].upper() for loan in new_loans}
    for book in bookCat:
        if book["bookID"].upper() not in still_loaned_bookids:
            book["status"] = "available"

    with open(data_file("bookCatalogues.txt"), "w", encoding="utf-8") as file:
        for book in bookCat:
            file.write(f"{book['bookID']};{book['title']};{book['author']};{book['status']}\n")


def update_profile():
    global login_user
    print("\nCurrent profile information")
    print("===========================")
    print(f"UserID: {login_user['userID']}, Username: {login_user['username']}, Password: {login_user['password']}")

    new_name = input("Enter new username (or press Enter to keep the current name): ").strip()
    new_password = input("Enter new password (or press Enter to keep the current password): ").strip()

    if new_name:
        login_user["username"] = new_name
    if new_password:
        login_user["password"] = new_password

    newList = mem_list()
    with open(data_file("member_info.txt"), "w", encoding="utf-8") as file:
        for member in newList:
            if member["userID"].upper() == login_user["userID"].upper():
                file.write(f"{login_user['userID']};{login_user['username']};{login_user['password']}\n")
            else:
                file.write(f"{member['userID']};{member['username']};{member['password']}\n")

    print("\nProfile updated! Here is the updated information:")
    print("=================================================")
    print(f"UserID: {login_user['userID']}, Username: {login_user['username']}, Password: {login_user['password']}")


def search_bookCat():
    print("\nBook Catalogues")
    print("===============")
    mylist = book_list()
    no = 1
    for book in mylist:
        print(f"{no}. BookID: {book['bookID']}")
        no += 1

    search = input("Enter the bookID/title/author to search (or enter EXIT): ").strip()
    if search.upper() == "EXIT":
        return

    book_found = []
    for book in mylist:
        if (
            book["bookID"].upper() == search.upper()
            or book["title"].lower() == search.lower()
            or book["author"].lower() == search.lower()
        ):
            book_found.append(book)

    if book_found:
        for book in book_found:
            print(f"BookID: {book['bookID']}, Title: {book['title']}, Author: {book['author']}, Status: {book['status']}")
    else:
        print("Book Not Found!")
        return search_bookCat()


# =========================
# Entry point
# =========================
if __name__ == "__main__":
    choose_char()
