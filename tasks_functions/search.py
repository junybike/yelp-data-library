# TO SEARCH BUSINESS(ES) WITH SPECIFIC CRITERIA
def business(conn):

    print("\n=====DATABASE BUSINESS SEARCH=====")
    print("*Leave sections blank if certain criteria is not needed*\n")

    # Set minimum star to search. Default minstar: 0
    minstar = input("Set minimum stars (0 - 5): ")
    if not minstar:
        minstar = 0
    elif minstar < "0" or minstar > "5":
        print("star must be between 0 and 5")
        return False

    # Set city, search for a name (or part of the name), and set sort option.
    city = input("Set city location: ")
    name = input("The business name to search: ")
    sortoption = input("Sort by... 1. name 2. city 3. star (1 - 3): ")

    # sortoption default: name
    if not sortoption:
        sortoption = "name"
    else:
        match int(sortoption):
            case 0:
                sortoption = "name"
            case 1:
                sortoption = "name"
            case 2:
                sortoption = "city"
            case 3:
                sortoption = "stars"

    # SQL query
    cursor = conn.cursor(as_dict=True)
    cursor.execute(
        """
        SELECT *
        FROM dbo.Business
        WHERE stars >= %s
        AND upper(city) like concat('%', upper(%s), '%')
        AND upper(name) like concat('%', upper(%s), '%')
        ORDER BY %s
        """,
        params = (float(minstar), city, name, sortoption)
    )

    i = 0
    row = cursor.fetchone()

    # To display the result.
    if row is not None:
        while row is not None:
            print("row " + str(i + 1) + ": ", row)
            i += 1

            if (i % 10 == 0):
                if (int(input("\nType 1 to continue, 0 to stop ")) == 0):
                    break
                print("\n")
            row = cursor.fetchone()
    else:
        print("\nNo such Business found!")

    return True


# TO SEARCH USER(S) WITH SPECIFIC CRITERIA
def users(conn):

    print("\n=====DATABASE USER SEARCH=====")
    print("*Leave section blank if certain criteria is not needed*\n")

    # Set the minimum review count of the user. Default: 0
    mincount = input("Set minimum review count: ")
    if not mincount:
        mincount = 0
    elif mincount < "0" or mincount > "9999999999":
        print("Review count must be greater than or equal to 0 ")
        return False

    # Set the minimum average star of the user. Default: 0
    minavgstar = input("Set minimum average star: ")
    if not minavgstar:
        minavgstar = 0
    elif minavgstar < "0" or minavgstar > "5":
        print("star must be between 0 and 5")
        return False

    # To search a name (or part of the name)
    name = input("User name to search: ")

    # SQL query
    cursor = conn.cursor(as_dict=True)
    cursor.execute(
        """
        SELECT *
        FROM dbo.user_yelp
        WHERE review_count >= %s
        AND average_stars >= %s
        AND upper(name) like concat('%', upper(%s), '%') 
        ORDER BY name
        """,
        params = (int(mincount), float(minavgstar), name)
    )

    i = 0
    row = cursor.fetchone()

    # To display the result.
    if row is not None:
        while row is not None:
            print("row " + str(i + 1) + ": ", row)
            i += 1

            if (i % 10 == 0):
                if (int(input("\nType 1 to continue, 0 to stop ")) == 0):
                    break
                print("\n")
            row = cursor.fetchone()
    else:
        print("\nNo such user found!")

    return True