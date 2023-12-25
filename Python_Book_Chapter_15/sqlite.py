import sqlite3

#####################################
# Create and manage a db connection #
#####################################
# connect to an exisitng db or create a new one:
# in the current work directory
# connection_1 = sqlite3.connect("test_db.db")
# in a different directory (specify the full path)
# connection_2 = sqlite3.connect("C:\\Users\\mjarz\\PycharmProjects\\Python-exercises-Z2J\\test_database.db")
# in memory - when data needs to exist (be cached) only when the app runs
# connection_3 = sqlite3.connect(":memory:")
# to interact with the db (create tables, execute queries, etc.) - create a cursor:
# cursor = connection_1.cursor()
# example query
# query = "SELECT datetime('now', 'localtime');"
# result = cursor.execute(query)
# row = result.fetchone()
# date = row[0]
# print(date)
# close the db connection
# connection_1.close()

###################################################
# Manage the db connection using a context manager #
###################################################

# with sqlite3.connect("example_db.db") as example_connection:
#     cursor = example_connection.cursor()
#     query = "SELECT datetime('now', 'localtime');"
#     result = cursor.execute(query)
#     row = result.fetchone()
#     time = row[0]
# print(time)

# any changes made to the db are saved automatically when managing the connection with a context manager

#######################
# Working with tables #
#######################

## Without a context manager:

# connection = sqlite3.connect("test_db_1.db")
# cursor = connection.cursor()
# create_table = ("""CREATE Table People
#                (FirstName TEXT,
#                LastName TEXT,
#                Age INT);""")
# insert_values = ("""INSERT INTO People VALUES "
#                      ('Ron', "
#                      'Obvious',
#                      42);""")
# cursor.execute(create_table)
# cursor.execute(insert_values)
# connection.commit()
# connection.close

## Using a context manager

# with sqlite3.connect("test_db.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("""DROP TABLE IF EXISTS People;""")
#     # create_table = ("""CREATE TABLE People
#     #            (FirstName TEXT,
#     #            LastName TEXT,
#     #            Age INT);""")
#     # insert_values = ("""INSERT INTO People VALUES "
#     #                  ('Ron', "
#     #                  'Obvious',
#     #                  42);""")
#     # cursor.execute(create_table)
#     # cursor.execute(insert_values)
#     query = "SELECT * FROM People"
#     result = cursor.execute(query)
#     row = result.fetchone()
#     print(row)

# Execute a script with .executescript(script)
#
# script = """
# DROP TABLE IF EXISTS People;
# CREATE TABLE People (
#     FirstName TEXT,
#     LastName TEXT,
#     Age INT
# );
# INSERT INTO People VALUES(
#     'Ron',
#     'Pauly',
#     42
# );
# """
# with sqlite3.connect("new_db.db") as connection:
#     cursor = connection.cursor()
#     cursor.executescript(script)

# execute many similar statements with .executemany(tuple_of_tuples)

# people_values =(
#     ('Ron', 'Pauly', 42),
#     ('John','Snow', 38),
#     ('Arthur','Andersen', 55)
# )
#
# create_table = ("""CREATE TABLE IF NOT EXISTS People
#            (FirstName TEXT,
#            LastName TEXT,
#            Age INT);""")
# with sqlite3.connect("people_db.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute(create_table)
#     cursor.executemany("INSERT INTO People VALUES (?, ?, ?)", people_values)
#     query = "SELECT FirstName, LastName, Age FROM People"
#     result = cursor.execute(query).fetchall()
#     for row in result:
#         print(row)

# new_connection = sqlite3.connect("people_db.db")
# cursor = new_connection.cursor()
# cursor.execute("""
# UPDATE People SET Age=? WHERE FirstName=? AND LastName=?;""",
#                (45, 'Arthur', 'Andersen'))
# new_connection.commit()
# query = """SELECT FirstName, LastName, Age FROM People WHERE LastName='Andersen';"""
# result = cursor.execute(query).fetchall()
# for row in result:
#     print(row)
# new_connection.close()

### REVIEW EXERCISES
# """
# (1) Create a new db with a table named 'Roster' that has 3 fields: Name, Species, Age
#  The Name and Species columns should be text fields, and the Age column should be an integer field"""
# create_table = """
#         CREATE TABLE IF NOT EXISTS Roster (
#         'Name' TEXT,
#         'Species' TEXT,
#         'Age' INT
#         );
#         """
# """
# (2) Populate your new table with the following values:
# """
# values = (
#     ('Benjamin', 'Human', 40),
#     ('Jadzia', 'Trill', 300),
#     ('Kira', 'Bajoran', 29)
# )
# """
# (3) Update the Name of Jadzia to be Ezri
# (4) Display the Name and Age of everyone in the table classified as Bajoran
# """
#
# with sqlite3.connect("animals.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("DROP TABLE IF EXISTS Roster;")
#     cursor.execute(create_table)
#     cursor.executemany("INSERT INTO Roster VALUES(?, ?, ?);", values)
#     cursor.execute("UPDATE Roster SET Name=?, Species=?, Age=? WHERE Name='Jadzia'", ('Ezri', 'Trill', 300))
#     # test_results = cursor.execute("SELECT * FROM Roster;").fetchall()
#     # for result in test_results:
#     #     print(result)
#     query = ("""SELECT
#                 Name,
#                 Species,
#                 Age FROM Roster
#                 WHERE Species='Bajoran'""")
#     result = cursor.execute(query).fetchone()
#     print(result)

