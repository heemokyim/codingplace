# PostgreSQL = import psycopg2

# sudo service postgresql start

import psycopg2
# you can work with PostgreSQL with terminal
# but that's pretty burdensome
# why don't you use library for programming language?

conn = psycopg2.connect("dbname='postgres' user='postgres' password='postgres1324' host='localhost' port='5432'")
# Load if there else Make one

cur = conn.cursor()

def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER,price REAL)")

    conn.commit()


def insert(item,quantity,price):
    # cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item,quantity,price))
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price))

    conn.commit()

def select():
    cur.execute("SELECT * FROM store")

    rows = cur.fetchall()

    print(rows)

    conn.commit()

def delete(item):
                                    # When only 1, put comma to its end
    cur.execute("DELETE FROM store WHERE item='%s'" % (item))

    conn.commit()

def update(quantity,price,item):
    cur.execute("UPDATE store SET quantity='%s', price ='%s' WHERE item='%s'" % (quantity,price,item))

    conn.commit()
    
create_table()
insert("Wine glass",100,5)
# delete("Wine glass")
update(2222,5.55,'Wine glass')
select()

conn.close()
