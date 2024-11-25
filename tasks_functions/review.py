from datetime import datetime

# FUNCTION DEFINITION
# To review a business
def business(conn, userid):

    print("\n=====DATABASE REVIEW BUSINESS=====")
    businessid = input("Enter the Business ID to review: ")

    # SQL Query to check if the 'businessid' exists in the database.
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

    # Displays the info of business with the 'businessid'.
    print("\nThe business information:")
    print(row, "\n")

    # The user rates the business.
    rate = input("Rate star for the business (1 - 5): ")
    if not rate:
        print("\nInvalid input :(")
        return False  
    elif rate < "1" or rate > "5":
        print("\nInvalid input :(")
        return False

    # The new review ID generated for this review.
    reviewid = userid[-3:] + str(datetime.now())[:-7]
    print("\nThe new review ID: \n" + reviewid)

    # SQL Query to insert the new review to the database.
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
