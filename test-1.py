import mysql.connector as sql

Server = sql.connect(host = 'localhost',
    user = 'root',
    passwd='sqlx',
    db='Student' )

cur = Server.cursor()

# WHERE condition
SNo = int(input("Enter the Sno. of the Student to Update: "))

# SET value01
ColumnName = input("Enter the Name of the Column to Update: ")

#SET value02
NewValue = input("Enter the New Value: ")

cur.execute(f"UPDATE Table01 SET {ColumnName}='{NewValue}' WHERE Sno={SNo};")
Server.commit()

cur.execute(f"Select * from Table01;")
Data = cur.fetchall()
for i1 in Data:
    for i2 in range (0, len(i1)):
        print(f"{i1[i2]} \t", end='')
    print()


cur.close()