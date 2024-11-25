# FUNCTION DEFINITION:
# To add a friendship with another user in the database
def friend(conn, userid):

    print("\n=====DATABASE MAKE FRIEND=====")
    friendwith = input("Enter the user ID to be friend with: ")

    # To not allow to add a friendship with the user themselves.
    if friendwith == userid:
        print("\nCannot friend your self!")
        return False

    # SQL Query to check if the 'friendwith' exists in the database.
    cursor = conn.cursor(as_dict=True)
    cursor.execute(
        """
        SELECT * 
        FROM dbo.user_yelp
        WHERE user_id = %s
        """,
        params = friendwith
    )

    row = cursor.fetchone()
    if row is None:
        print("\nNo user exists!")
        return False

    # SQL Query to check if the user already has a friendship with a user with the 'friendwith' user ID
    cursor = conn.cursor(as_dict=True)
    cursor.execute(
        """
        SELECT * 
        FROM dbo.friendship
        WHERE user_id = %s
        AND friend = %s
        """,
        params = (userid, friendwith)
    )

    # To not allow the duplicate friendship
    newrow = cursor.fetchone()
    if newrow is not None:
        print("\nYou are already friends with this user!")
        return False

    # Displays the info of user with 'friendwith' user ID  
    print("\nThe user information:")
    print(row)

    # Confirmation
    confirm = input("Add friend with the user? (1. yes, 0. no): ")
    if confirm != "1":
        print("Make friend cancelled!")
        return False

    # SQL Query to insert a new friendship
    cursor = conn.cursor(as_dict=True)
    cursor.execute(
        """
        INSERT INTO dbo.friendship(user_id, friend)
        VALUES(%s, %s)
        """,
        (userid, friendwith)
    )
    conn.commit()

    print("\nMake friend successful!")

    return True

