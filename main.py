
from library import Library
lib=Library()
lib.load_books()
lib.load_users()
while True:
    print("1.add book")
    print("2.add user")
    print("3.issue book")
    print("4.return book")
    print("5.show books")
    print("6.show users")
    print("7. exit")

    x=input("ENTER YOUR CHOICE")

    if x=="1":
        lib.add_book()
        lib.save_books()
    elif x=="2":
        lib.add_user()
        lib.save_users()
    elif x=="3":
        lib.issue_book()
        lib.save_books()
        lib.save_users()
    elif x=="4":
        lib.return_book()
        lib.save_books()
        lib.save_users()
    elif x=="5":
        lib.show_books()
    elif x=="6":
        lib.show_users()
    elif x=="7":
        print("program exited")
        break
else:
    print("INVALID CHOICE")