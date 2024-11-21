from tasks_functions import make, review, search


# Displays the choices of option available
def display_menu():
    print("=====DATABASE MENU=====")
    print("1. Search Business")
    print("2. Search Users")
    print("3. Make Friend")
    print("4. Review Business")
    print("0. Exit")

# Executes the chosen task
def execute_task(conn, option, userid):
    success = True
    match option:
        case 1:
            success = search.business(conn)
        case 2:
            success = search.users(conn)
        case 3:
            success = make.friend(conn, userid)
        case 4:
            success = review.business(conn)

    return success