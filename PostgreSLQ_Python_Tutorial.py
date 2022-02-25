import psycopg2
import pandas as pd

#Create a connection to the DB
con = psycopg2.connect(
    host = 'localhost',
    database = 'baseball',
    user = '',
    password = '')

# Create a cursor to acess the information from the DB
cur = con.cursor()

cur.execute('''

    SELECT * FROM salaries
    LIMIT 10;

'''
)

rows = cur.fetchall()

for r in rows:
    df = pd.DataFrame(r)

# Close de cursor
cur.close()
#Close de connection
con.close()

print(df)
