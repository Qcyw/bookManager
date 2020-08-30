
import sqlite3


# initial setups
conn = sqlite3.connect('book.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS books (
                book_id INTEGER PRIMARY key AUTOINCREMENT,
                book_name text,
                author text,
                year integer,
                ISBN real
            )""")


def view_all():
    list = []
    c.execute("SELECT * FROM books")
    for i in c.fetchall():
        list.append(str(i[0]) + ". " + i[1] + " {" + i[2] + "} " + str(i[3]) + " " + str(i[4]))
    return list


def add_book(book_name, author, year, ISBN):
    with conn:
        c.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, ?)",
            (book_name, author, year, ISBN))


def delete_book(id):
    with conn:
        book = view_all()[id]
        c.execute("DELETE from books WHERE book_id = ? ", (book[0],))


def clear():
    with conn:
        c.execute("DELETE FROM books")


def search_book(title, author, year, ISBN):
    list = []
    c.execute("SELECT * FROM books where book_name like ? and author like ? or ISBN = ? ", (title, author, ISBN))
    for i in c.fetchall():
        list.append(str(i[0]) + ". " + i[1] + " {" + i[2] + "} " + str(i[3]) + " " + str(i[4]))
    return list


