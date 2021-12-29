# This is the top class library in the world
class Library:
    Books=["The rich dad and the Poor dad", "The Great Gatsby", "Sex Education", "The lord of the rings", "Game of thrones"]
    def __init__(self,ListofBooks,Library_name):
        self.ListOfBooks=ListofBooks
        self.LibraryName=Library_name

    def __init__(self):
        pass

    def displayBook(self):
        print(f"The available books are:\n{self.Books}\n")
    @classmethod
    def lendBook(cls,name,bookName):
        cls.name=name
        cls.bookName=bookName

        if bookName in cls.Books:
            print(f"The book \"{cls.bookName}\" is lended for {cls.name}\n")
            cls.Books.remove(cls.bookName)
        else:
            print("The requested book is not available..please lend the books from the availables list..")


    def addBook(self,name,bookName):
        self.name=name
        self.bookName=bookName
        self.Books.append(self.bookName)
        print(f"The book {self.bookName} has been added to the library by {self.name}\n")

    def returnBook(self,name,bookName):
        self.name="karthik"
        self.bookName=bookName
        self.Books.append(self.bookName)
        print(f"The book {self.bookName} has been returned by {self.name}\n")


# one=Library()
# one.lendBook("karthik","Game of thrones")
# one.displayBook()
# one.addBook("The witcher")
# one.displayBook()
# one.returnBook("karthik","Game of thrones")
# one.displayBook()
while True:
    print("Welcome to our Library..we provide you the following services\nEnter...")
    print("1=> Display the available books list")
    print("2=> If your interested in lending the book")
    print("3=> If you wanna donate books to our library")
    print("4=> To return the book")
    print("5=> To exit from our library")
    choice=int(input("Enter your choice.."))
    if choice == 1:
        lib_assistent=Library()
        lib_assistent.displayBook()
    elif choice == 2:
        lib_assistent = Library()
        name=input("Enter your name")
        bookName=input("Enter the book name")
        lib_assistent.lendBook(name,bookName)
    elif choice==3:
        lib_assistent = Library()
        name = input("Enter your name")
        bookName = input("Enter the book name")
        lib_assistent.addBook(name, bookName)
    elif choice == 4:
        lib_assistent = Library()
        name = input("Enter your name")
        bookName = input("Enter the book name")
        lib_assistent.returnBook(name, bookName)
    elif choice==5:
        print("Thank you for visiting our library..")
        exit()

    else:
        print("Enter a valid choice..\n")
