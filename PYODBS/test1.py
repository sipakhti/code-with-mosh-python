import pyodbc

conn = pyodbc.connect("Driver={SQL Server};"
                      "Server=SIPAKHTI\SQLEXPRESS;"
                      "Database=Std_Ref_Food;"
                      "Trusted_Connection=yes;")

cursor = conn.cursor()


cursor.execute("SELECT TOP(1000) * From Std_Ref_Food.dbo.Food_Desc ")

for row in cursor:
    print(row)
