import pyodbc

SERVER = 'DESKTOP-SBSRJFQ\\SQLEXPRESS'
DATABASE = 'LoginCharp'
Trusted_Connection = 'yes'

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection={Trusted_Connection}'
conn = pyodbc.connect (connectionString)

Query="""
SELECT ID,Username, Telephone, Password
FROM Users 
ORDER BY ID;
"""

cursor= conn.cursor()
cursor.execute(Query)

records=cursor.fetchall()
for r in records:
    print(f"\t{r.ID}\t{r.Username}\t{r.Telephone}\t{r.Password}")