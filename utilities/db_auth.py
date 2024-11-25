def login(conn):

    attempt = 0

    while attempt < 3:

        print("=====DATABASE LOGIN=====")
        print("Enter your user ID. (attempts:" + str(attempt + 1) + "/3)")
        userid = input("ID: ")

        cursor = conn.cursor(as_dict=True)
        cursor.execute(
            'SELECT user_id \
            FROM dbo.user_yelp \
            WHERE user_id = %s',
            params = userid
        )

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
