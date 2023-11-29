import sqlite3

con = sqlite3.connect('films_db.sqlite')

cur = con.cursor()

req = '''SELECT title FROM films
    WHERE title LIKE "%?"'''
res = cur.execute(req).fetchall()
for i in res:
    print(i[0])

con.close()