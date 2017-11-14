# sqlite = import sqlite3 (builtin)
# PostgreSQL = import psycopg2

import sqlite3

# Controller of SQLite == Cursor
# Cursor points certain row of table
# This is why SQLite is called embedded SQL because of Cursor


# 1. Connect to databse == sqlite3.connect
# 2. Create cursor      == conn.cursor()
# 3. Do SQL             == cursor.execute()
# 4. Do Commit          == conn.commit()
# 5. Close connection   == conn.close()

# PRIMARY KEY == UNIQUE + NOT NULL
def create_table(conn,cur):
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER,price REAL)")

    conn.commit()


def insert(conn,cur,item,quantity,price):
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))

    conn.commit()

def select(conn,cur):
    cur.execute("SELECT * FROM store")

    rows = cur.fetchall()

    print(rows)

    conn.commit()

def delete(conn,cur,item):
                                    # When only 1, put comma to its end
    cur.execute("DELETE FROM store WHERE item=?",(item,))

    conn.commit()

def update(conn,cur,quantity,price,item):
    cur.execute("UPDATE store SET quantity=?, price =? WHERE item=?",(quantity,price,item))

conn = sqlite3.connect('lite.db')
# Load if there else Make one

cur = conn.cursor()

create_table(conn,cur)
# insert(conn,cur,"Wine glass",100,5)
# delete(conn,cur,"Water glass")
update(conn,cur,2222,5.55,'Wine glass')
select(conn,cur)

conn.close()
