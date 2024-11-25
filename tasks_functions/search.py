# FUNCTION DEF:
# TO SEARCH BUSINESS(ES) WITH SPECIFIC CRITERIA
def business(conn):

    print("\n=====DATABASE BUSINESS SEARCH=====")
    print("*Leave sections blank if certain criteria is not needed*\n")

    # Set minimum star to search. Default minstar: 0
    minstar = input("Set minimum stars (1 - 5): ")
    if not minstar:
        minstar = 0
    elif minstar < "1" or minstar > "5":
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

    # SQL Query to get all businesses that matches the criteria.
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

    i = 0 # A counter
    row = cursor.fetchone() # The first info of the business fetched from the database

    # To display the result. It displays maximum 10 businesses at a time.
    if row is not None:
        while row is not None:
            print("row " + str(i + 1) + ": ", row)
            i += 1

            # Asks the user if they want more businesses to be displayed
            if i % 10 == 0:
                if input("\nType 1 to continue, 0 to stop ") != "1":
                    break
                print("\n")
            row = cursor.fetchone()
    else:
        print("\nNo such Business found!")

    return True



# FUNCTION DEF:
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

    # A name to search (or part of the name)
    name = input("User name to search: ")

    # SQL Query to search a user that matches the criteria.
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

    i = 0 # A counter
    row = cursor.fetchone() # The info of the first user fetched from the database.

    # To display the result. It displays maximum 10 users at a time.
    if row is not None:
        while row is not None:
            print("row " + str(i + 1) + ": ", row)
            i += 1

            # Asks the user if they want more businesses to be displayed
            if i % 10 == 0:
                if int(input("\nType 1 to continue, 0 to stop ")) == 0:
                    break
                print("\n")
            row = cursor.fetchone()
    else:
        print("\nNo such user found!")

    return True
