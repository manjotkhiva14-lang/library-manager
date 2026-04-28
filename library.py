
from book import Book
from user import User
import json
class Library:
    def __init__(self):
        self.books=[]
        self.users=[]
    def get_valid_int(self,prompt):
        while True:
            try:
                value = int(input(prompt))
                if value <= 0:
                    print("Enter the valid number")
                    continue
                return value
            except ValueError:
                print("Invalid input. Enter the number")
    def get_valid_string(self,prompt):
        while True:
            value = input(prompt).strip()
            if value == "" :
                print("empty input")
                continue
            return value
    def add_book(self):
        while True:
            title= self.get_valid_string("enter the title of the book")
            if any(book.title.lower() == title.lower() for book in self.books):
                print("This book title already exits")
                continue
            break
        author= self.get_valid_string("enter the author of the book")
        while True:
            bookid=self.get_valid_int("enter the id of the book")
            if any(book.bookid == bookid for book in self.books):
                print("This book id is not available. Try another")
                continue
            break
        book= Book(title,author,bookid)
        self.books.append(book)


    def add_user(self):
        user=self.get_valid_string("enter the name of the user")
        while True:
            userid=self.get_valid_int("enter the id of the user")
            if any(user.userid == userid for user in self.users):
                print("This user id is not available. Try another")
                continue
            break
        user= User(user,userid)
        self.users.append(user)

    def issue_book(self):
        id=self.get_valid_int("enter the id of the book you want to issue")
        userid=self.get_valid_int("enter the user id to whom you want to issue book")
        bf= None
        for book in self.books:
            if book.bookid==id:
                bf = book
                break
        if bf is None:
            print("Book not found")
            return
        if not bf.available:
            print("Book is already issued")
            return
        uf= None
        for user in self.users:
            if user.userid==userid:
                uf = user
                break
        if uf is None:
            print("User not found")
            return
        uf.borrowedbooks.append(bf)
        bf.available=False
        print(f"the book {bf.title} is isuued to {uf.name}")
    def return_book(self):
        id=self.get_valid_int("enter the id of the book")
        userid=self.get_valid_int("enter the user id ")
        bf= None
        for book in self.books:
            if book.bookid==id:
                bf = book
                break
        if bf is None:
            print("Book not found")
            return
        if bf.available:
            print("Book is already returned")
            return
        uf = None
        for user in self.users:
            if user.userid==userid:
                uf = user
                break
        if uf is None:
            print("User not found")
            return
        uf.borrowedbooks.remove(bf)
        bf.available=True
        print(f"the book {bf.title} is returned by {uf.name}")
    
    def show_books(self):
        if not self.books:
            print("no books available")
            return
        for book in self.books:
            print(f"Name : {book.title}")
            print(f"Author name:{book.bookauthor}")
            print(f"Id : {book.bookid}")
            print(f"Available:{book.available}")
    def show_users(self):
        if not self.users:
            print("no users available")
            return
        for user in self.users:
            print(f"Name:{user.name}")
            print(f"Id :{user.userid}")
            if user.borrowedbooks:
                print("Borrowed books are:")
                for book in user.borrowedbooks:
                    print(f" {book.title}")
            else:
                print("Borrowed books:none")
    def save_books(self):
        data=[]

        for book in self.books:
            data.append({
                "title":book.title,
                "bookauthor":book.bookauthor,
                "bookid":book.bookid,
                "available":book.available
            })
        with open("books.json" , "w" )as file:
            json.dump(data,file,indent=4)
        
        print("books saved successfully")
    def load_books(self):
        try:
            with open("books.json" , "r") as file:
                books = json.load(file)
               
            for b in books:
                book=Book(b["title"], b["bookauthor"], b["bookid"])
                book.available=b["available"]
                self.books.append(book)
            print("Books loaded successfully")
        except FileNotFoundError:
            print("previous data not found")
        except json.JSONDecodeError:
            print("file is empty, starting fresh")
    def save_users(self):
        data=[]
        for user in self.users:
            user_data = ({
                "name": user.name,
                "userid": user.userid,
                "borrowed books": []
            })
            for book in user.borrowedbooks:
                user_data["borrowed books"].append(book.bookid)
            data.append(user_data)
        with open("users.json" , "w")as file:
            json.dump(data,file,indent=4)
        
    def load_users(self):
        try:
            with open("users.json" , "r")as file:
                users = json.load(file)
            book_dict={}
            for book in self.books:
                book_dict[book.bookid]= book

            for u in users:
                user = User(u["name"] , u["userid"])
                user.borrowedbooks=[]
            
                for book_id in u["borrowed books"]:
                    book = book_dict.get(book_id)
                    if book:
                        user.borrowedbooks.append(book)
                self.users.append(user)
            print("users loaded successfully")
        except FileNotFoundError:
            print("no file found")
