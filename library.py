
from book import Book
from user import User
import json
class Library:
    def __init__(self):
        self.books=[]
        self.users=[]

    def add_book(self):
        tittle=input("enter the tittle of the book")
        author=input("enter the author of the book")
        bookid=int(input("enter the id of the book"))
        book= Book(tittle,author,bookid)
        self.books.append(book)


    def add_user(self):
        user=input("enter the name of the user")
        userid=int(input("enter the id of the user"))
        user= User(user,userid)
        self.users.append(user)

    def issue_book(self):
        id=int(input("enter the id of the book you want to issue"))
        userid=int(input("enter the user id to whom you want to issue book"))
        bf= None
        uf= None
        for book in self.books:
            if book.bookid==id:
                bf = book
        for user in self.users:
            if user.userid==userid:
                uf = user
        if bf and uf:
            uf.borrowedbooks.append(bf)
            bf.available=False
            print(f"the book {bf.tittle} is isuued to {uf.name}")
        else:
            print("invalid input")
    def return_book(self):
        id=int(input("enter the id of the book"))
        userid=int(input("enter the user id to whom you want to issue book"))
        bf= None
        uf= None
        for book in self.books:
            if book.bookid==id:
                bf = book
        for user in self.users:
            if user.userid==userid:
                uf = user
        if bf and uf:
            uf.borrowedbooks.remove(bf)
            bf.available=True
            print(f"the book {bf.tittle} is returned by {uf.name}")
        else:
            print("invalid input")
    def show_books(self):
        if not self.books:
            print("no books available")
            return
        for book in self.books:
            print(f"Name : {book.tittle}")
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
                    print(f" {book.tittle}")
            else:
                print("Borrowed books:one")
    def save_books(self):
        data=[]

        for book in self.books:
            data.append({
                "tittle":book.tittle,
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
                book=Book(b["tittle"], b["bookauthor"], b["bookid"])
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
            print("users loaded")
        except FileNotFoundError:
            print("no file found")
