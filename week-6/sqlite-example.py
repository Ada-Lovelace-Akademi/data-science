import sqlite3
import random

def random_int():
    return(random.randint(1, 100))

my_list = [
    (random_int(), "apple", "red"),
    (random_int(), "banana", "yellow"),
    (random_int(), "cherry", "red"),
    (random_int(), "date", "brown"),
    (random_int(), "grape", "purple"),
    (random_int(), "kiwi", "brown"),
    (random_int(), "lemon", "yellow"),
    (random_int(), "orange", "orange"),
    (random_int(), "pear", "green"),
    (random_int(), "watermelon", "green")
]

# create connection
connection = sqlite3.connect("fruits.db")

# create cursor object
cursor = connection.cursor()

cursor.execute("CREATE TABLE fruits (amount interger, fruit text, color text)")

# insert data to table
cursor.executemany("INSERT INTO fruits VALUES (?,?,?)", my_list)

# print database rows
for row in cursor.execute("SELECT * FROM fruits"):
    print(row)

print("\n")

# print spesific rows
cursor.execute("SELECT * FROM fruits WHERE color=:c", {"c": "green"})
color_search = cursor.fetchall()
print(color_search)

# new table
print("\n")
cursor.execute("CREATE TABLE translates (en_color text, tr_color text)")
cursor.execute("INSERT INTO translates VALUES (?,?)", ("green", "yeşil"))
cursor.execute("SELECT * FROM translates WHERE en_color=:c", {"c": "green"})
translate_search = cursor.fetchall()  
print(translate_search)

# manipulate database
print("\n")
for data in color_search:
    qs = [translate_search[0][1] if value==translate_search[0][0] else value for value in data]
    print(qs)

connection.close()
