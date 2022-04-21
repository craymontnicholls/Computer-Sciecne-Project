import tkinter as tk

def show_frame(frame):
    frame.tkraise()


import mysql.connector
from mysql.connector import Error
import pandas as pd



pw = "Password123!"
db = "preschool"

#function that connects to the SQl workbench database
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


connection = create_server_connection("localhost", "root", pw)

create_server_connection("localhost", "root", pw)

#function that creates the database from statemnt below
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


create_database_query = "CREATE DATABASE preschool"
create_database(connection, create_database_query)


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")









create_child_table = """
CREATE TABLE child (
  child_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  age INT


  );
 """

create_parent_table = """
CREATE TABLE parent (
    parent_id INT PRIMARY KEY,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL

    );
   """

create_bills_table = """
CREATE TABLE bills (
    bills_id INT PRIMARY KEY,
    weekly_hours INT,
    grant_hours INT
    
    );
    """

alter_bills = """
ALTER TABLE bills
ADD FOREIGN KEY(child)
REFERENCES client(child_id)
ON DELETE SET NULL;
"""

pop_parent = """
INSERT INTO parent VALUES
(1,  'J', 'Smith'),
(2, 'S',  'Martin' ), 
(3, 'S', 'Wang'),
(4, 'F',  'Müller-Rossi'),
(5, 'I', 'Ivanova'),
(6, 'S', 'Murphy');
"""

pop_child = """
INSERT INTO child VALUES
(1,  'James', 'Smith', 3),
(2, 'Stefanie',  'Martin', 3 ), 
(3, 'Steve', 'Wang', 3),
(4, 'Friederike',  'Müller-Rossi', 4),
(5, 'Isobel', 'Ivanova', 4),
(6, 'Niamh', 'Murphy', 2);
"""

pop_bills = """
INSERT INTO bills VALUES
(1 , 20 , 1 ),
(2 , 32 , 0 ),
(3 , 10 , 0 ),
(4 , 30 , 1 ),
(5 , 24 , 0);

"""

connection = create_db_connection("localhost", "root", pw, db)  # Connect to the Database
execute_query(connection, create_child_table)  # Execute our defined query
execute_query(connection, create_parent_table)

execute_query(connection, create_bills_table)
execute_query(connection, alter_bills)
execute_query(connection, pop_parent)
execute_query(connection, pop_child)

execute_query(connection, pop_bills)


def insert_into_c(connection, dict):


    cursor = connection.cursor()
    try:
        sql_statement = "INSERT INTO child(child_id, first_name, last_name,age) VALUES (%s,%s,%s,%s)"
        values = (dict['childs_key'],dict['first_name'],dict['last_name'],dict['age'])



        cursor.execute(sql_statement,values)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")



def execute_list_query(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


sql1 = '''
    INSERT INTO parent(parent_id, first_name, last_name) 
    VALUES (%s, %s, %s)
    '''

val1 = [
    (7, 'Hank', 'Dodson'),
    (8, 'Sue', 'Perkins')
]

sql2 = '''
    INSERT INTO bills(bills_id, weekly_hours, grant_hours) 
    VALUES (%s, %s, %s)
    '''

val2 = [
    (7, 26, 1),
    (8, 31, 0)
]

sql3 = '''
    INSERT INTO bills(bills_id, weekly_hours, grant_hours) 
    VALUES (%s, %s, %s)
    '''

val3 = [
    (9, 30, 0),

]


sql4 = '''
    INSERT INTO bills(bills_id, weekly_hours, grant_hours) 
    VALUES (%s, %s, %s)
    '''

val4 = [
    (10, 22, 0),

]

sql5 = '''
    INSERT INTO parent(parent_id, first_name, last_name) 
    VALUES (%s, %s, %s)
    '''

val5 = [
    (9, 'Jon', 'Dawson'),

]


sql6 = '''
    INSERT INTO bills(child_id, first_name, last_name,age) 
    VALUES (%s, %s, %s,%s)
    '''

val6 = [
    (7, 'Toby', 'Perkins',3),
]

sql7 = '''
    INSERT INTO bills(bills_id, weekly_hours, grant_hours) 
    VALUES (%s, %s, %s)
    '''

val7 = [
    (11, 20, 0),

]
sql8 = '''
    INSERT INTO parent(parent_id, first_name, last_name) 
    VALUES (%s, %s, %s)
    '''

val8 = [
    (10, 'Steven', 'White'),

]

execute_list_query(connection, sql8, val8)

sql9 = '''
    INSERT INTO child(child_id, first_name, last_name,age) 
    VALUES (%s, %s, %s,%s)
    '''

val9 = [
    (8, 'Toby', 'Dawson',3),
]

execute_list_query(connection, sql9, val9)

execute_list_query(connection, sql7, val7)


connection = create_db_connection("localhost", "root", pw, db)
execute_list_query(connection, sql1, val1)
execute_list_query(connection, sql2, val2)
execute_list_query(connection, sql3, val3)
execute_list_query(connection, sql6, val6)
execute_list_query(connection, sql5, val5)
execute_list_query(connection, sql4, val4)


#function that reads the queries described below
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

#queries that are used by the funtion to read from the database

q1 = """
SELECT *
FROM child;
"""

q2 = """
SELECT *
FROM parent;
"""

q4 = """
SELECT * 
FROM bills;
"""

calculation1 = """
SELECT Weekly_Hours
FROM bills
WHERE GRANT_HOURS = 0;

"""

calculation2 = """
SELECT Weekly_Hours
FROM bills
WHERE GRANT_HOURS > 0;

"""
connection = create_db_connection("localhost", "root", pw, db)
results = read_query(connection, q1)
results2 = read_query(connection, q2)
c1 = read_query(connection, calculation1)
c2 = read_query(connection, calculation2)
results4 = read_query(connection, q4)

print(c1)

#takes the result from calculation1 and calculation2

list_of_numbers1 = []
for integer in c1:
    number = integer[0]
    list_of_numbers1.append(number)

print(list_of_numbers1)

list_of_numbers2 = []
for integer in c2:
    number = integer[0]
    list_of_numbers2.append(number)

print(list_of_numbers2)

#takes the results
x = sum(list_of_numbers1)
y = sum(list_of_numbers2)
ans = str(x - y)










from_db = []

# Loop over the results and append them into our list

# Returns a list of tuples
for result in results:
    result = result
    from_db.append(result)

# Initialise empty list
from_db = []

# Loop over the results and append them into our list

# Returns a list of tuples
for result in results:
    result = list(result)
    from_db.append(result)

columns = ["child_id", "first_name", "last_name", "age"]
df = pd.DataFrame(from_db, columns=columns)

print(df)

# prints for the second query

print("")

from_db = []

# Loop over the results and append them into our list

# Returns a list of tuples
for result2 in results2:
    result2 = result2
    from_db.append(result2)

# Initialise empty list
from_db = []

# Loop over the results and append them into our list

# Returns a list of tuples
for result2 in results2:
    result = list(result2)
    from_db.append(result)

columns = ["parent_id", "first_name", "last_name"]
df2 = pd.DataFrame(from_db, columns=columns)

print(df2)

# prints for the third query

print("")

from_db = []

# Loop over the results and append them into our list

# Returns a list of tuples
for result4 in results4:
    result4 = result4
    from_db.append(result4)

# Initialise empty list
from_db = []

for result4 in results4:
    result = list(result4)
    from_db.append(result4)

columns = ["bills_id", "weekly_hours", "grant_hours"]
df4 = pd.DataFrame(from_db, columns=columns)

print(df4)



#Line between Database and GUI ---------------------------------------------------------------------------------------------




window = tk.Tk()
window.state('zoomed')
window.geometry("300x250")
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)
frame4 = tk.Frame(window)
frame5 = tk.Frame(window)
frame6 = tk.Frame(window)
frame7 = tk.Frame(window)
frame8 = tk.Frame(window)
frame9 = tk.Frame(window)
frame10 = tk.Frame(window)

for frame in (frame1,frame2,frame3,frame4,frame5,frame6,frame7,frame8,frame9, frame10):
    frame.grid(row=0, column = 0, sticky = 'nsew')



#Frame1 -------------- Code


frame1_title = tk.Label(frame1,text="BillsCalc", bg="grey",height = '10' ,font = ("Calibre", 20))
frame1_title.pack(fill = 'x')


frame1_btn1 = tk.Button(frame1,text="Login", height = '5', width = '15',font = ("Calibre", 15),command =lambda:show_frame(frame3))
frame1_btn1.pack(pady = 150)

frame1_btn2 = tk.Button(frame1,text="Register",height = '5', width = '15',font = ("Calibre", 15),command =lambda:show_frame(frame2))
frame1_btn2.pack()
#Frame2 -----------------
frame2_title=tk.Label(frame2, text="Enter Details", bg="grey", width="300", height="2", font=("Calibre", 16))
frame2_title.pack()


frame2_l1=tk.Label(frame2,text="Username * ")
frame2_l1.pack()
frame2_user_entry = tk.Entry(frame2)
frame2_user_entry.pack()
frame2_l2=tk.Label(frame2, text="Password * ").pack()
frame2_password_entry = tk.Entry(frame2)
frame2_password_entry.pack()

frame2_btn1 = tk.Button(frame2, text="Register", width="20", height="2", command =lambda:show_frame(frame1)).pack()

#Frame3 -----------------
frame3_title=tk.Label(frame3, text="Enter Details", bg="grey", width="300", height="2", font=("Calibre", 16))
frame3_title.pack()


frame3_l1=tk.Label(frame3,text="Username * ")
frame3_l1.pack()
frame3_user_entry = tk.Entry(frame3)
frame3_user_entry.pack()
frame3_l2=tk.Label(frame3, text="Password * ").pack()
frame3_password_entry = tk.Entry(frame3)
frame3_password_entry.pack()

frame3_btn1 = tk.Button(frame3, text="Login", width="20", height="2", command =lambda:show_frame(frame4)).pack()

#Frame4 ---------------------------------

frame4_title = tk.Label(frame4, text="Home", bg="grey", width="300", height="6" ,font=("Calibre", 16))
frame4_title.pack()

frame4_btn1 = tk.Button(frame4, text="Enter Calculator", width="30", height="4",command =lambda:show_frame(frame5))
frame4_btn1.pack(pady = 100)

frame4_btn2 = tk.Button(frame4, text="Enter new Data", width="30", height="4", command =lambda:show_frame(frame7))
frame4_btn2.pack(pady = 100)

frame4_btn3 = tk.Button(frame4, text="Enter Database", width="30", height="4", command =lambda:show_frame(frame6))
frame4_btn3.pack(pady = 100)

frame4_btn4 = tk.Button(frame4, text ="back", command = lambda:show_frame(frame3))
frame4_btn4.pack()

#Frame5 ----------------------------

frame5_title = tk.Label(frame5, text = "Calculator", bg = "grey", width ="300", height="6", font =("Calibre", 16))
frame5_title.pack()

frame5_btn1 = tk.Button(frame5, text="Calculate total amount due", width="30", height="4")
frame5_btn1.pack(pady = 100)

frame5_l1 = tk.Label(frame5, text="Total amount due is £"+ ans,font =("Calibre", 16))
frame5_l1.pack(pady = 100)

frame5_btn2 = tk.Button(frame5, text ="back", command = lambda:show_frame(frame4))
frame5_btn2.pack()

#Frame6 ---------------------------

frame6_btn1 = tk.Button(frame6, text = "Display database", width="30", height="4")
frame6_btn1.pack(pady = 200)

frame6_title = tk.Label(frame6, text = "Database will be displayed in command window ", bg = "grey", width ="300", height="5", font =("Calibre", 16))
frame6_title.pack(pady = 160, fill = 'y')

frame6_btn2 = tk.Button(frame6, text ="back", command = lambda:show_frame(frame4))
frame6_btn2.pack()

#Frame7 -------------------------------

frame7_title =  tk.Label(frame7, text="Which Data to Enter?", bg="grey", width="300", height="6" ,font=("Calibre", 16))
frame7_title.pack()

frame7_btn1 = tk.Button(frame7, text="Child Data",width="30", height="4",command =lambda:show_frame(frame8))
frame7_btn1.pack(pady = 100)

frame7_btn2 = tk.Button(frame7, text="Parent Data",width="30", height="4", command =lambda:show_frame(frame9))
frame7_btn2.pack(pady = 100)

frame7_btn3 = tk.Button(frame7, text="Billing Data",width="30", height="4", command =lambda:show_frame(frame10))
frame7_btn3.pack(pady = 100)

frame7_btn4 = tk.Button(frame7, text ="back", command = lambda:show_frame(frame4))
frame7_btn4.pack()



#Frame8 -------------------







frame8_title =  tk.Label(frame8, text="Entering Child data", bg="grey", width="300", height="6" ,font=("Calibre", 16))
frame8_title.pack()

frame8_l1 = tk.Label(frame8, text = "Childs Key")
frame8_l1.pack()
frame8_e1 = tk.Entry(frame8)
frame8_e1.pack()

frame8_l2 = tk.Label(frame8, text = "First Name")
frame8_l2.pack()
frame8_e2 = tk.Entry(frame8)
frame8_e2.pack()


frame8_l3 = tk.Label(frame8, text = "Last Name")
frame8_l3.pack()
frame8_e3 = tk.Entry(frame8 )
frame8_e3.pack()



frame8_l4 = tk.Label(frame8, text = "age")
frame8_l4.pack()
frame8_e4 = tk.Entry(frame8)
frame8_e4.pack()

entries_child = {'childs_key':frame8_e1,'first_name':frame8_e2,'last_name':frame8_e3,'age':frame8_e4}

frame8_btn1 = tk.Button(frame8, text = "Input Data")
frame8_btn1.pack()

frame8_btn2 = tk.Button(frame8, text ="back", command = lambda:show_frame(frame7))
frame8_btn2.pack()



#Frame 9 ------------------------------------



frame9_title =  tk.Label(frame9, text="Entering Parent data", bg="grey", width="300", height="6" ,font=("Calibre", 16))
frame9_title.pack()

frame9_l1 = tk.Label(frame9, text = "Parent Key")
frame9_l1.pack()
frame9_e1 = tk.Entry(frame9)
frame9_e1.pack()

frame9_l2 = tk.Label(frame9, text = "First Name")
frame9_l2.pack()
frame9_e2 = tk.Entry(frame9)
frame9_e2.pack()


frame9_l3 = tk.Label(frame9, text = "Last Name")
frame9_l3.pack()
frame9_e3 = tk.Entry(frame9)
frame9_e3.pack()

entries_parent = {'parent_id':frame9_e1,'first_name':frame9_e2,'last_name':frame9_e3}

frame9_btn1 = tk.Button(frame9, text = "Input Data")
frame9_btn1.pack()

frame9_btn2 = tk.Button(frame9, text ="back", command = lambda:show_frame(frame7))
frame9_btn2.pack()

#Frame 10 -------------------------------------
frame10_title =  tk.Label(frame10, text="Entering Bills data", bg="grey", width="300", height="6" ,font=("Calibre", 16))
frame10_title.pack()


frame10_l1 = tk.Label(frame10, text = "Billing Key")
frame10_l1.pack()
frame10_e1 = tk.Entry(frame10)
frame10_e1.pack()

frame10_l2 = tk.Label(frame10, text = "Weekly hours")
frame10_l2.pack()
frame10_e2 = tk.Entry(frame10)
frame10_e2.pack()

frame10_l3 = tk.Label(frame10, text = "Weekly Grant hours")
frame10_l3.pack()
frame10_e3 = tk.Entry(frame10)
frame10_e3.pack()

entries_bills = {'bills_id':frame10_e1,'weekly_hours':frame10_e2,'grant_hours':frame10_e3}

frame10_btn1 = tk.Button(frame10, text = "Input Data")
frame10_btn1.pack()


frame10_btn2 = tk.Button(frame10, text ="back", command = lambda:show_frame(frame7))
frame10_btn2.pack()









show_frame(frame1)
window.mainloop()