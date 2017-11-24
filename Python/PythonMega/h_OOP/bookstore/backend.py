import sqlite3

class Database:
    def __init__(self,dbPath):
        self.conn = sqlite3.connect(dbPath)
        self.cur = self.conn.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS bookstore (title TEXT, author TEXT, year INTEGER, ISBN TEXT)")
        self.conn.commit()

    def __del__(self):
        print("I'm here !")
        self.conn.close()

    def makeSelect(self,title="",author="",year="",ISBN=""):
        SQL =" WHERE"

        if title != "":
            SQL += " title='%s' AND" % title
        if author != "":
            SQL += " author='%s' AND" % author
        if year != "":
            SQL += " year=%d AND" % int(year)
        if ISBN != "":
            SQL += " ISBN='%s' AND" % ISBN

        SQL = SQL.rstrip("AND")

        return SQL

    def view(self):
        self.cur.execute("SELECT  rowid,title,author,year,ISBN FROM bookstore")
        rows = self.cur.fetchall()
        self.conn.commit()

        return rows

    def search(self,title="",author="",year="",ISBN=""):
        if (title+author+str(year)+ISBN)=="":
            self.view()
            return

        SQL="SELECT rowid,title,author,year,ISBN FROM bookstore"
        SQL+=self.makeSelect(title,author,year,ISBN)

        self.cur.execute(SQL)
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows

    def insert(self,title="",author="",year="",ISBN=""):
        SQL = "INSERT INTO bookstore VALUES('%s','%s',%d,'%s')" %(title,author,int(year),ISBN)

        self.cur.execute(SQL)
        self.conn.commit()

    # Need to be SQL trimmed for robust functionality
    def update(self,id,title,author,year,ISBN):
        SQL = "UPDATE bookstore SET title='%s', author='%s', year=%d, ISBN='%s' WHERE rowid=%d" %(title,author,int(year),ISBN,id)

        self.cur.execute(SQL)
        self.conn.commit()

    def delete(self,id):
        SQL = "DELETE FROM bookstore WHERE rowid=%d" % (id)

        self.cur.execute(SQL)
        self.conn.commit()
