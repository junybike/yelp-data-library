import pymssql
from utilities import db_auth, ui

# CONNECT TO THE DATABASE
conn = pymssql.connect(host='cypress.csil.sfu.ca', user='s_jla890',
                       password='66y2hd7JYFGGnQqh', database='jla890354')

# GET 3 USER INFO
cursor = conn.cursor(as_dict=True)
cursor.execute('SELECT TOP(3) * FROM dbo.User_yelp')
for row in cursor:
    print ('row:', row)

# LOGIN SECTION
userid = db_auth.login(conn)
if userid == 0:
    exit(0)

# SHOW MENU AND EXECUTE OPTION
option = -1
while True:

    # The user selects the task. (Refer to ui.py for the list of tasks)
    ui.display_menu()
    option = input("Enter the option (0 - 4): ")

    if not option and (option < "0" or option > "4"):
        print("Invalid option :( \n")
        continue
    elif option == "0":
        break

    if ui.execute_task(conn, int(option), userid):
        print("Task executed successfully :)\n")
    else:
        print("Task failed :( \n")

# EXITING
print("Exiting...")
exit(0)

# SAMPLE USER ID AND BUSINESS ID FOR TESTING PURPOSES
# __OdjK-F4MTdHkb8RtDFlQ
# cVBxfMC4lp3DnocjYA3FHQ
