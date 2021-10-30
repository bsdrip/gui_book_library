import sqlite3


class Database:

  def __init__(self,db):
    self.conn = sqlite3.connect(db)
    self.cur = self.conn.cursor()
    self.cur.execute("CREATE TABLE IF NOT EXISTS books_DB (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn TEXT)")
    self.conn.commit()

  def book_insert(self,title,author,year,isbn):
    self.cur.execute("INSERT INTO books_DB VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    self.conn.commit()

  def db_view(self):
    self.cur.execute("SELECT * FROM books_DB")
    rows = self.cur.fetchall()
    return rows

  def book_search(self,title="",author="",year="",isbn=""):
    self.cur.execute("SELECT * FROM books_DB WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows = self.cur.fetchall()
    return rows

  def book_delete(self,id):
    self.cur.execute("DELETE FROM books_DB WHERE id=?", (id,))
    self.conn.commit()

  def db_update(self,id,title,author,year,isbn):
    self.cur.execute("UPDATE books_DB SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn, id))
    self.conn.commit()

  def __del__(self):
    self.conn.close()
