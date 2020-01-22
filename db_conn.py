import mysql.connector
from mysql.connector import Error

dbUser = "root"
dbPass = ""
dbHost = "127.0.0.1"
dbName = "contacts_app"

def getContacts():
    conn = mysql.connector.connect(user=dbUser, passwd=dbPass, host=dbHost, db=dbName)

    cursor = conn.cursor()

    query = "SELECT * FROM contacts"

    cursor.execute(query)

    rs = cursor.fetchall()
    if len(rs) == 0:
        print("You have not contacts")

    for row in rs:
        print("******************************")
        print("Name: " + row[1] + " " + row[2])
        print("Age: " + str(row[3]))
        print("Phone: " + row[4])
        print("Email: " + row[5])
        print("******************************")

    cursor.close()
    conn.close()

def addContact():
    first = input("First Name: ")
    last = input("Last Name: ")
    age = int(input("Age: "))
    phone = input("Phone Number: ")
    email = input("Email: ")

    conn = mysql.connector.connect(user=dbUser, passwd=dbPass, host=dbHost, db=dbName)
    cursor = conn.cursor()

    query = "INSERT INTO contacts(first, last, age, phone, email) VALUES(%s, %s, %s, %s, %s)"
    vals = (first, last, age, phone, email)
    cursor.execute(query, vals)

    conn.commit()

    print(first + " " + last + " was added to your contacts")