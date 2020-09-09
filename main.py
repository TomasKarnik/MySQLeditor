
import mysql.connector

mydb = mysql.connector.connect(
  user='remote',
  password='test.test',
  host='localhost',
  database='db',

)
print(30 * '-')
print("   M A I N - M E N U")
print(30 * '-')
print("1. MySQL create table")
print("2. MySQL insert")
print("3. MySQL select")
print("4. MySQL Where")
print("5. MySQL order by")
print("6. MySQL Delete record")
print("7. MySQL Drop table")
print("8. MySQL Update")
print("8. Info")
print(30 * '-')

## Get input ###
choice = input('Enter your choice [1-9] : ')

### Convert string to int type ##
choice = int(choice)

### create table ###
if choice == 1:
  print("Create table")
  mycursor = mydb.cursor()
  text1 = input("name of the table:")
  var1=input("Varchar1 name:")
  var2 = input("Varchar2 name:")
  mycursor.execute("CREATE TABLE " + text1 + " (" + var1 + " VARCHAR(255), " + var2 + " VARCHAR(255))")
elif choice == 2: ### fill table ###
  mycursor = mydb.cursor()
  tablename=input("What would you like to fill table:")
  var1=input("Column1:")
  var2=input("Column1:")
  sql = "INSERT INTO " + tablename + " (" + var1 + ", " + var2 + ") VALUES (%s, %s)"
  value1 = input("Value to insert 1:")
  value2 = input("Value to insert 2:")
  val = (value1,value2)
  mycursor.execute(sql, val)
  mydb.commit()

  print(mycursor.rowcount, "record inserted.")
elif choice == 3:
  mycursor = mydb.cursor()
  tablename=input("Select table:")
  mycursor.execute("SELECT * FROM " + tablename + "")

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)
elif choice == 4: ### where ###
  mycursor = mydb.cursor()
  print("SELECT * FROM /table/ WHERE /column/ ='/your input/'")
  tablename=input("select table:")
  column=input("Select column:")
  var=input("Your input:")
  sql = "SELECT * FROM " + tablename + " WHERE " + column + " =" + column + ""

  mycursor.execute(sql)

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)
elif choice == 5: ### order by ###
  mycursor = mydb.cursor()
  print("SQL query will look like:SELECT * FROM /table name/ ORDER BY /column/")
  tablename=input("select table:")
  var=input("Select column:")
  sql = "SELECT * FROM " + tablename + " ORDER BY " + var + ""

  mycursor.execute(sql)

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)
elif choice == 6: ### delete record ###
  mycursor = mydb.cursor()
  print(" Your sql query will look like this:DELETE FROM /your table/ WHERE /your column/ = '/your input/'")
  tablename=input("Select table:")
  column=input("select column:")
  what=input("Your input:")
  sql = "DELETE FROM " + tablename + " WHERE " + column + " = '" + what + "'"

  mycursor.execute(sql)

  mydb.commit()

  print(mycursor.rowcount, "record(s) deleted")
elif choice == 7: ### drop table ###
  mycursor = mydb.cursor()
  print("Your query will look like this:DROP TABLE /your table/")
  tablename=input("Select table:")
  sql = "DROP TABLE " + tablename + ""

  mycursor.execute(sql)
elif choice == 8: ### update ###
  mycursor = mydb.cursor()
  tablename=input("Select table:")
  column=input("select column:")
  var2=input("From what")
  var1 = input("To what:")
  sql = "UPDATE " + tablename + " SET " + column + " = '" + var1 + "' WHERE " + column + " = '" + var2 + "'"

  mycursor.execute(sql)

  mydb.commit()

  print(mycursor.rowcount, "record(s) affected")
elif choice == 9:
  print("MySQL editor")
  print("------------")
  print("Created by Tomáš Kárník")
  print("https://github.com/TomasKarnik/MySQLeditor")
else:  ## if everything goes wrong ##
  print("Invalid number. Try again...")




