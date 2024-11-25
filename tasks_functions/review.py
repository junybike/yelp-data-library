from datetime import datetime

def check(conn):
    businessid = input("businessid: ")

    cursor = conn.cursor(as_dict=True)
    cursor.execute(
        """
        SELECT * 
        FROM dbo.business
        WHERE business_id = %s
        """,
        params = businessid
    )
    row = cursor.fetchone()
    if row is None:
        print("\nNo review exists!")
        return False

    print("\nThe review information:")
    print(row, "\n")

def test(conn, userid):
    reviewid = input("reviewid: ")
    businessid = input("businessid: ")

    cursor = conn.cursor(as_dict=True)
    cursor.execute(
        """
        SELECT * 
        FROM dbo.review
        WHERE business_id = %s
        AND review_id = %s
        AND user_id = %s
        """,
        params=(businessid, reviewid, userid)
    )

    row = cursor.fetchone()
    if row is None:
        print("\nNo review exists!")
        return False

    print("\nThe review information:")
    print(row, "\n")



def business(conn, userid):

    print("\n=====DATABASE REVIEW BUSINESS=====")

    businessid = input("Enter the Business ID to review: ")

    if businessid == "test":
        test(conn, userid)
        return 1
    if businessid == "check":
        check(conn)
        return 1

    cursor = conn.cursor(as_dict=True)
    cursor.execute(
        """
        SELECT * 
        FROM dbo.business
        WHERE business_id = %s
        """,
        params = businessid
    )

    row = cursor.fetchone()
    if row is None:
        print("\nNo business exists!")
        return False

    print("\nThe business information:")
    print(row, "\n")

    rate = input("Rate star for the business (1 - 5): ")
    if not rate:
        print("\nInvalid input :(")
        return False  
    elif rate < "1" or rate > "5":
        print("\nInvalid input :(")
        return False

    reviewid = userid[-3:] + str(datetime.now())[:-7]
    #reviewid = str(userid) + str(datetime.now())
    print("\nThe new review ID: \n" + reviewid)

    cursor = conn.cursor(as_dict=True)
    cursor.execute(
        """
        INSERT INTO dbo.review(review_id, user_id, business_id, stars)
        VALUES(%s, %s, %s, %s)
        """,
        (reviewid, userid, businessid, int(rate))
    )
    conn.commit()

    print("\nReview successful!\n")

    return True
