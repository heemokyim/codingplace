# sqlite = import sqlite3 (builtin)

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

conn = sqlite3.connect('lite.db')
# Load if there else Make one

cur = conn.cursor()

def create_table():
    # automatically pk made as rowid
    # no need to define additional primary key
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER,price REAL)")

    conn.commit()


def insert(item,quantity,price):
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))

    conn.commit()

def select():
    cur.execute("SELECT rowid,quantity FROM store")

    rows = cur.fetchall()

    print(rows)

    conn.commit()

def delete(item):
                                    # When only 1, put comma to its end
    cur.execute("DELETE FROM store WHERE item=?",(item,))

    conn.commit()

def update(quantity,price,item):
    cur.execute("UPDATE store SET quantity=?, price =? WHERE item=?",(quantity,price,item))

create_table()
insert("Wine glass",100,5)
# delete("Water glass")
update(2222,5.55,'Wine glass')
select()

conn.close()
