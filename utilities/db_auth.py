# FUNCTION DEF
# Login system for the database.
def login(conn):

    # If a user enters non-existing ID 3 times, shuts off the system.
    attempt = 0
    while attempt < 3:

        print("=====DATABASE LOGIN=====")
        print("Enter your user ID. (attempts:" + str(attempt + 1) + "/3)")
        userid = input("ID: ")

        # To handle inputting nothing in 'userid'
        if not userid:
            print("Invalid user ID :(\n")
            attempt += 1
            if attempt >= 3:
                print("Too many attempts :( Shutting down...")
                return 0
            continue

        # SQL Query to check if 'ID' exists in database.
        cursor = conn.cursor(as_dict=True)
        cursor.execute(
            """
            SELECT user_id 
            FROM dbo.user_yelp 
            WHERE user_id = %s
            """,
            params = userid
        )

        # If the 'cursor' finds the ID in database, return the userid. Else, return 0.
        row = cursor.fetchone()
        if row is not None:
            print("Login successful :)\n")
            return userid
        else:
            print("Invalid user ID :(\n")
            attempt += 1
            if attempt >= 3:
                print("Too many attempts :( Shutting down...")
                return 0
