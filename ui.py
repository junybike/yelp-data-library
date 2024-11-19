import make
import search
import review

def display_menu():
    print("=====DATABASE MENU=====")
    print("1. Search Business")
    print("2. Search Users")
    print("3. Make Friend")
    print("4. Review Business")
    print("0. Exit")

def execute_task(option, conn):
    match option:
        case "1":
            search.business(conn)
        case "2":
            search.users(conn)
        case "3":
            make.friend(conn)
        case "4":
            review.business(conn)