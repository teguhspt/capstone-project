import getpass # mengambil input password dari pengguna dan menyembunyikan input tersebut saat dimasukkan.

# Data Dummy
libraryBooks = [
    {'id': 'FKS-001', 'title': 'Kubunuh Disini', 'author': 'Soe Tjen Marching', 'genre':'FIksi', 'available': True},
    {'id': 'NFK-001', 'title': 'Move On', 'author': 'Ely Susanti', 'genre':'Non Fiksi', 'available': False},
    {'id': 'NFK-002', 'title': 'Young On Top', 'author': 'Billy Boen', 'genre':'Non Fiksi', 'available': True},
    {'id': 'FKS-002', 'title': 'Garis Waktu', 'author': 'Fiersa Besari', 'genre':'Fiksi', 'available': True},
    {'id': 'NFK-003', 'title': 'Y', 'author': 'Billy Boen', 'genre':'Non Fiksi', 'available': True},
    {'id': 'NFK-004', 'title': 'Satelite', 'author': 'Tim Penulis ASSI', 'genre':'Non Fiksi', 'available': False}
]

# Read Function
def displayBooks(books):
    if not books:
        print("There are no books in the library.\n")
    else:
        print("\n","-"*90)
        print(f"|{'List of Books':^89}|")
        print("","-"*90)
        print(f"| {'ID':^7} | {'Title':^18} | {'Auothor':^20} | {'Genre':^15} | {'Status':^15} | ")
        print("","-"*90)
        for book in books:
            availability = "Available" if book['available'] else "Not Available"
            print(f"| {book['id']:^7} | {book['title']:^18} | {book['author']:^20} | {book['genre']:^15} | {availability:^15} | ")

# Create Function
def addBook(books, id, title, author, genre):
    new_book = {
        'id': id,
        'title': title,
        'author': author,
        'genre' : genre,
        'available': True
    }
    books.append(new_book)
    print("\n","-"*90)
    print(f"| {'=== The book' + ' (' + title + ') ' + 'has been added to the Library ===':^88} |")
    print("","-"*90)  

# Update Book from Title
def updateBookFromTitle(books, new_title):
    for book in books:
        if book['id'].lower() == id.lower():
            book['title'] = new_title
            print("\n","-"*90)
            print(f"| {'Book information with ID' + ' ' + id + ' ' + 'has been updated':^88} |")
            print("","-"*90)
            return
    print("\n","-"*90)
    print(f"| {'Book information with ID' + '' + id + '' + 'not found!' :^88} |")
    print("","-"*90,"\n")

def updateBookFromAuthor(books, new_author):
    for book in books:
        if book['id'].lower() == id.lower():
            book['author'] = new_author
            print("\n","-"*90)
            print(f"| {'Book information with ID' + ' ' + id + ' ' + 'has been updated':^88} |")
            print("","-"*90)
            return
    print("\n","-"*90)
    print(f"| {'Book information with ID' + '' + id + '' + 'not found!' :^88} |")
    print("","-"*90,"\n")


def updateBookFromGenre(books, new_genre):
    for book in books:
        if book['id'].lower() == id.lower():
            book['genre'] = new_genre
            print("\n","-"*90)
            print(f"| {'Book information with ID' + ' ' + id + ' ' + 'has been updated':^88} |")
            print("","-"*90)
            return
    print("\n","-"*90)
    print(f"| {'Book information with ID' + '' + id + '' + 'not found!' :^88} |")
    print("","-"*90,"\n")

# Delete Function
def deleteBook(books, book_id):
    for book in books:
        if book['id'].lower() == book_id.lower():
            books.remove(book)
            print("\n","-"*90)
            print(f"| {'Book information with ID' + '' + book_id + '' + 'has been removed from the library' :^88} |")
            print("","-"*90,"\n")
            return
    print("\n","-"*90)
    print(f"| {'Book information with ID' + '' + book_id + '' + 'not found!' :^88} |")
    print("","-"*90,"\n")

# Search Function by Title
def searchByTitle(title, listBooks):
    bookFound = None
    for book in listBooks:
        if book['title'].lower() == title.lower():
            bookFound = book
            break
    return bookFound

# Search Function by ID
def searchByID(id, listBooks):
    bookFoundID = None
    for book in listBooks:
        if book['id'].lower() == id.lower():
            bookFoundID = book
            break
    return bookFoundID

# Implementasi
while True:
    try:
        print("\n","="*90)
        print(f"| {'=== PURWADHIKA MINI LIBRARY ===':^88} |")
        print("","="*90)
        print(f"| {'[1] Display Book List':<88} |")
        print(f"| {'[2] Add New Book':<88} |")
        print(f"| {'[3] Update Book Information':<88} |")
        print(f"| {'[4] Delete Book':<88} |")
        print(f"| {'[0] Exit':>88} |")
        print("","="*90,"\n")

        selectMenu = int(input("Select Menu> "))
        if selectMenu == 1:
            while True:
                print("\n","-"*90)
                print(f"| {'Display Book List Menu':^88} |")
                print("","-"*90)              
                print(f"| {'[1] View All Books':<88} |\n| {'[2] Search by ID':<88} |\n| {'[3] Search by Title':<88} |")
                print("","-"*90,"\n") 
                subMenu = input("Select Sub Menu ('q' to back)> ")
                if subMenu == 'q':
                    break            
                elif subMenu =='1':
                    displayBooks(libraryBooks)
                    print("","-"*91) 
                    while True:                   
                        subMenuChoice = input("\n'q' to Back> ")
                        if subMenuChoice !="q":
                            print("\n","-"*90) 
                            print(f"| {'!!! Only accepts q input !!!':^89}|")
                            print("","-"*90)
                        else:
                            break
                elif subMenu == '2':
                    while True:
                        id = input("\nEnter the ID ('q' to back)> ")
                        if id == 'q':
                            break
                        searchResult = searchByID(id, libraryBooks)  
                        if searchResult:
                            print("\n","-"*90)
                            print(f" | {'Book ID':<10}{':':<2}{searchResult['id']:<76} |")
                            print(f" | {'Title':<10}{':':<2}{searchResult['title']:<76} |")
                            print(f" | {'Author':<10}{':':<2}{searchResult['author']:<76} |")
                            print(f" | {'Genre':<10}{':':<2}{searchResult['genre']:<76} |")
                            if searchResult['available']:
                                print(f" | {'=== Book Available ===':^88} |")
                                print(" ","-"*90)
                            else:
                                print(f" | {'=== Sorry, Book isnt Available ===':^88} |")
                                print(" ","-"*90)
                        else:
                            print("\n","-"*90) 
                            print(f"| {'== Book not found! ==':^89}|")
                            print("","-"*90)

                elif subMenu == '3':
                    while True:
                        bookTitle = input("\nEnter the title ('q' to back)> ")
                        if bookTitle == 'q':
                            break
                        searchResult = searchByTitle(bookTitle, libraryBooks)  
                        if searchResult:   
                            print("\n","-"*90)
                            print(f" | {'Book ID':<10}{':':<2}{searchResult['id']:<76} |")
                            print(f" | {'Title':<10}{':':<2}{searchResult['title']:<76} |")
                            print(f" | {'Author':<10}{':':<2}{searchResult['author']:<76} |")
                            print(f" | {'Genre':<10}{':':<2}{searchResult['genre']:<76} |")
                            if searchResult['available']:
                                print(f" | {'=== Book Available ===':^88} |")
                                print(" ","-"*90)
                            else:
                                print(f" | {'=== Sorry, Book isnt Available ===':^88} |")
                                print(" ","-"*90)
                        else:
                            print("\n","-"*90) 
                            print(f"| {'== Book not found! ==':^89}|")
                            print("","-"*90)    
                else:
                    print("Your input isn't Available")    
        elif selectMenu == 2:
            print("\nLogin as Admin to Add new Book\n")
            while True:
                username = input("Username: ")
                password = getpass.getpass("Password: ")
                if username == "admin" and password == "manager":
                    print("\n","-"*90)
                    print(f"| {'=== Login Successfully ===':^88} |")
                    print(f"| {'=== Please enter the details of the book you want to add ===':^88} |")
                    print("","-"*90, "\n")
                    id = input("Input Book ID : ")             
                    title = input("Input Book Title: ")
                    author = input("Input Book Author : ")
                    genre = input("Input Book Genre: ")
                    print("\n","-"*90)
                    print(f"| {'Book Information: ':^88} |")
                    print("","-"*90) 
                    print(f"| {'Book ID':<10}{':':<2}{id.upper():<76} |")
                    print(f"| {'Title':<10}{':':<2}{title.capitalize():<76} |")
                    print(f"| {'Author':<10}{':':<2}{author.capitalize():<76} |")
                    print(f"| {'Genre':<10}{':':<2}{genre.capitalize():<76} |")
                    print("","-"*90)
                    choice = input("Are you sure wanna add the book to the Library? (y/n): ")
                    if choice == "y":
                        addBook(libraryBooks, id, title, author, genre)
                        break
                    elif choice == "n":
                        print("\n","-"*90)
                        print(f"| {'=== The book' + ' (' + title + ') ' + 'was not added to the Library ===':^88} |")
                        print("","-"*90)  
                        break
                else:
                    print("\n","-"*90)
                    print(f"| {'== The Username or Password you entered is incorrect! ==':^88} |")
                    print("","-"*90,"\n")  
                    while True:
                        choice = input("Try Again? (y/n): ")
                        if choice == "y":
                            print("\n","-"*90)
                            print(f"| {'== Please input the correct username & password! ==':^88} |")
                            print("","-"*90,"\n")
                            break
                        elif choice == "n":
                            break
                        else:
                            print("Invalid choice!\n")
                    if choice == 'n':
                        break
        elif selectMenu == 3:
            displayBooks(libraryBooks)
            print("","-"*91) 
            while True:                
                id = input("\nEnter Book ID you want to update ('q' for exit): ")
                if id == 'q':
                    break            
                searchResult = searchByID(id, libraryBooks)  
                if searchResult:   
                    print("\n","-"*90)
                    print(f"| {'Book Information about' + ' ' + searchResult['id']:^88} |")
                    print("","-"*90)
                    print(f"| {'[1] Title':<12}{':':<2}{searchResult['title']:<74} |")
                    print(f"| {'[2] Author':<12}{':':<2}{searchResult['author']:<74} |")
                    print(f"| {'[3] Genre':<12}{':':<2}{searchResult['genre']:<74} |")
                    print("","-"*90)
                    while True:
                        choice = input("\nEnter the option you want to Update ('q' for exit): ")
                        if choice == 'q':
                            break
                        elif choice == "1":
                            new_title = input("\nInput new Title: ")
                            updateBookFromTitle(libraryBooks, new_title)
                            break
                        elif choice == "2":
                            new_author = input("\nInput new Author: ")
                            updateBookFromAuthor(libraryBooks, new_author)
                            break
                        elif choice == "3":
                            new_genre = input("\nInput a new genre: ")
                            updateBookFromGenre(libraryBooks, new_genre)
                            break
                        else:
                            print("\n","-"*90)
                            print(f"| {'The option you want to update is not available.':^88} |")
                            print("","-"*90)                           
                else:
                    print("\n","-"*90) 
                    print(f"| {'== Book not found! ==':^89}|")
                    print("","-"*90) 
        elif selectMenu == 4:
            displayBooks(libraryBooks)
            print("","-"*91) 
            while True:                
                book_id = input("\nEnter the ID of the book you want to delete ('q' for exit): ")
                if book_id == 'q':
                    break 
                searchResult = searchByID(book_id, libraryBooks)  
                if searchResult:   
                    print(" ","-"*90)
                    print(f" | {'Book ID':<10}{':':<2}{searchResult['id']:<76} |")
                    print(f" | {'Title':<10}{':':<2}{searchResult['title']:<76} |")
                    print(f" | {'Author':<10}{':':<2}{searchResult['author']:<76} |")
                    print(f" | {'Genre':<10}{':':<2}{searchResult['genre']:<76} |")
                    if searchResult['available']:
                        print(f" | {'=== Book Available ===':^88} |")
                        print(" ","-"*90)
                    else:
                        print(f" | {'=== Sorry, Book isnt Available ===':^88} |")
                        print(" ","-"*90)
                    subMenuChoice = input("Are you sure you want to delete the book from the Library? (y/n): ")
                    if subMenuChoice == "y":
                        deleteBook(libraryBooks, book_id)
                        break
                    elif subMenuChoice == "n":
                        print("\n","-"*90) 
                        print(f"| {'== Wanna try others ID? ==':^89}|")
                        print("","-"*90)  
                else:
                    print("\n","-"*90) 
                    print(f"| {'== Book not found! ==':^89}|")
                    print("","-"*90)          
        elif selectMenu == 0:
            print("\n","-"*90)
            print(f"| {'=== Thank you for using Purwadhika Mini Library! ===':^88} |")
            print("","-"*90)
            print("\n")
            break
        else:
            print("\n","^"*90) 
            print(f"| {'!!! The menu you entered is not available !!!':^89}|")
            print("","*"*90)
    except:
        print("\n","^"*90) 
        print(f"| {'!!! The option you entered is not valid!!!':^89}|")
        print("","*"*90)