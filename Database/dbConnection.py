import mysql.connector
# from ElectionData import data


# database connection established
db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="indianelection"
)

# to execute multiple query in one go we need to set buffered to true
my_cursor = db.cursor(buffered=True)