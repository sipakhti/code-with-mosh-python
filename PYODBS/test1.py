import pyodbc
from decimal import Decimal

conn = pyodbc.connect("Driver={SQL Server};"
                      "Server=SIPAKHTI\SQLEXPRESS;"
                      "Database=Std_Ref_Food;"
                      "Trusted_Connection=yes;")

cursor = conn.cursor()

test = "BUTTER"
cursor.execute(
    f"select TOP(12) Shrt_desc, Nutr_val, Units, Nutrdesc from food_desc inner join NUT_DATA on NUT_DATA.NDB_No=food_desc.NDB_No inner join Nutr_Def on Nutr_Def.Nutr_No=NUT_DATA.Nutr_No where shrt_desc like '%{test}%' ")

print(cursor)
for row in cursor:
    print(*row)

class Food:
    import pyodbc
    from decimal import Decimal

    conn = pyodbc.connect("Driver={SQL Server};"
                      "Server=SIPAKHTI\SQLEXPRESS;"
                      "Database=Std_Ref_Food;"
                      "Trusted_Connection=yes;")

    cursor = conn.cursor()
    
    desc = []
    dic = {}
    def __init__(self, test):
        cursor.execute(
            f"select TOP(12) Nutr_val, Units, Nutrdesc from food_desc inner join NUT_DATA on NUT_DATA.NDB_No=food_desc.NDB_No inner join Nutr_Def on Nutr_Def.Nutr_No=NUT_DATA.Nutr_No where shrt_desc like '%{test}%' ")

        for row in cursor:
            Food.desc.append(row)
            Food.dic[row[-1]] = row[: -1]
        




test1 = Food("BUTTER,WITH SALT")

print(test1.desc)
print(test1.dic)

for key, value in test1.dic.items():
    print(type(value[0]))
    print(value[0])
        
            

print(test1.dic)

