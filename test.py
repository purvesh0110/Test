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

cur.close()