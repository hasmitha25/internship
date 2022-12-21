import sqlite3  
  
# Creates and connects to a database 'sqlite.db'
import pdb; pdb.set_trace()
conn = sqlite3.connect('sqlite.db')  
print("Opened database successfully")

# Create a table 'Employees'
"""try:
    conn.execute('''CREATE TABLE Employees
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
except:
    # pass exception if table already exists
    pass
print("Table created successfully")
  
# insert some rows to the Employees table
conn.execute("INSERT INTO Employees (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Ajeet', 27, 'Delhi', 20000.00 )");  
  
conn.execute("INSERT INTO Employees (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 22, 'London', 25000.00 )");
  
conn.execute("INSERT INTO Employees (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Vikas', 29, 'Hyderabad', 30000.00 )");  
  
conn.execute("INSERT INTO Employees (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Kanchan', 22, 'Ghaziabad ', 25000.00 )");  
  
# commit the change
conn.commit()  
print("Records inserted successfully")
"""
data = conn.execute("select * from Employees");

for row in data:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

conn.close()  
