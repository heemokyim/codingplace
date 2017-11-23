import sqlite3

# 1. Connect to databse == sqlite3.connect
# 2. Create cursor      == conn.cursor()
# 3. Do SQL             == cursor.execute()
# 4. Do Commit          == conn.commit()
# 5. Close connection   == conn.close()

conn = sqlite3.connect('lite.db')

cur = conn.cursor()

def makeSelect(title="",author="",year="",ISBN=""):
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

def createTable():
    cur.execute("CREATE TABLE IF NOT EXISTS bookstore (title TEXT, author TEXT, year INTEGER, ISBN TEXT)")

    conn.commit()

def view():
    cur.execute("SELECT  rowid,title,author,year,ISBN FROM bookstore")

    rows = cur.fetchall()

    conn.commit()

    return rows

def search(title="",author="",year="",ISBN=""):
    if (title+author+str(year)+ISBN)=="":
        view()
        return

    SQL="SELECT rowid,title,author,year,ISBN FROM bookstore"

    SQL+=makeSelect(title,author,year,ISBN)

    cur.execute(SQL)

    rows = cur.fetchall()

    conn.commit()

    return rows

def insert(title="",author="",year="",ISBN=""):
    SQL = "INSERT INTO bookstore VALUES('%s','%s',%d,'%s')" %(title,author,int(year),ISBN)

    cur.execute(SQL)

    conn.commit()

# Need to be SQL trimmed for robust functionality
def update(id,title,author,year,ISBN):
    SQL = "UPDATE bookstore SET title='%s', author='%s', year=%d, ISBN='%s' WHERE rowid=%d" %(title,author,int(year),ISBN,id)

    cur.execute(SQL)

    conn.commit()

def delete(id):
    SQL = "DELETE FROM bookstore WHERE rowid=%d" % (id)

    cur.execute(SQL)

    conn.commit()
