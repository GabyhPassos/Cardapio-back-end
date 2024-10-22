import pyodbc

SERVER = 'DESKTOP-SBSRJFQ\\SQLEXPRESS'
DATABASE = 'Cardapioapp'
Trusted_Connection = 'yes'

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection={Trusted_Connection}'
conn = pyodbc.connect (connectionString)

Query="""
SELECT ID,Itemorder, Price, Amount
FROM ItemTeste
ORDER BY ID;
"""

cursor= conn.cursor()
cursor.execute(Query)

records=cursor.fetchall()
for r in records:
    print(f"\t{r.ID}\t{r.Itemorder}\t{r.Price}\t{r.Amount}")