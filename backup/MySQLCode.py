from time import time
import mysql.connector
import ElectionData
from selenium import webdriver
db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="election-data"
)

my_cursor = db.cursor()

add_candidate = ("INSERT INTO candidates"
                 "(Name,Party,Status,State,Constituency,Election,Election_Type)"
                 "values(%(Name)s,%(Party)s,%(Status)s,%(State)s,%(Constituency)s,%(Election)s,%(ElectionType)s)" )

ElectionData.main()
for candidate in ElectionData.data:
    my_cursor.execute(add_candidate,candidate)

db.commit()
my_cursor.close()
db.close()