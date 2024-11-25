def friend(conn, userid):

    print("\n=====DATABASE MAKE FRIEND=====")

    friend = input("Enter the user ID to be friend with: ")
    if (friend == userid):
        print("\nCannot friend your self!")
        return False

    cursor = conn.cursor(as_dict=True)
    cursor.execute(
        """
        SELECT * 
        FROM dbo.user_yelp
        WHERE user_id = %s
        """,
        params=(friend)
    )

    row = cursor.fetchone()
    if (row is None):
        print("\nNo user exists!")
        return False

    cursor = conn.cursor(as_dict=True)
    cursor.execute(
        """
        SELECT * 
        FROM dbo.friendship
        WHERE user_id = %s
        AND friend = %s
        """,
        params=(userid, friend)
    )
    newrow = cursor.fetchone()
    if (newrow is not None):
        print("\nYou are already friends with this user!")
        return False

    print("\nThe user information:")
    print(row)

    confirm = input("Add friend with the user? (1. yes, 0. no): ")
    if (confirm != "1"):
        print("Make friend cancelled!")
        return False

    cursor = conn.cursor(as_dict=True)
    cursor.execute(
        """
        INSERT INTO dbo.friendship(user_id, friend)
        VALUES(%s, %s)
        """,
        (userid, friend)
    )
    conn.commit()

    print("\nMake friend successful!")

    return True

