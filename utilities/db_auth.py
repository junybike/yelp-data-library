def login(conn):

    login = False
    attempt = 0

    while (not login):

        print("=====DATABASE LOGIN=====")
        print("Enter your user ID. (attempts:" + str(attempt + 1) + "/3)")
        userid = input("ID: ")

        cursor = conn.cursor(as_dict=True)
        cursor.execute(
            'SELECT user_id \
            FROM dbo.user_yelp \
            WHERE user_id = %s',
            params=(userid))

        row = cursor.fetchone()
        if row is not None:
            login = True
            print("Login successful :)\n")
            return 1
        else:
            print("Invalid user ID :(\n")
            attempt += 1
            if attempt >= 3:
                print("Too many attempts :( Shutting down...")
                return 0