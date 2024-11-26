import mysql.connector

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from subprocess import call

def Ok():
    mysqldb = mysql.connector.connect(host='localhost',username='root',password='ASdf@2004',database='project')
    my_cursor=mysqldb.cursor()
    uname = e1.get()
    password = e2.get()
    
    sql = "select * from login where username = %s and password = %s"
    my_cursor.execute(sql, [(uname), (password)])
    res=my_cursor.fetchall()
    if res:
        def ADD():     #inserts a record
            def tab2():
                def insert():
                    mysqldb = mysql.connector.connect(host='localhost',username='root',password='ASdf@2004',database='project')
                    my_cursor=mysqldb.cursor()
                    eid=e1.get()
                    ename=e2.get()
                    edept=e3.get()
    
                    sql = "insert into employee (empid, emp_name, emp_dept) values (%s, %s, %s)"
                    my_cursor.execute(sql, [(eid), (ename), (edept)])
                    
                    mysqldb.commit()
                    print(my_cursor.rowcount, "record inserted")
                    messagebox.showinfo("","Record Inserted Successfully!")

                def cancel():
                    root.destroy()
    
                root = Tk()
                root.title("Insert")
                root.geometry("360x200")
    
                global e1
                global e2
                global e3

                Label(root, text="Employee ID").place(x=10, y=10)
                Label(root, text="Employee Name").place(x=10, y=40)
                Label(root, text="Employee Dept").place(x=10, y=70)

                e1=Entry(root)
                e1.place(x=140, y=10)

                e2=Entry(root)
                e2.place(x=140, y=40)

                e3=Entry(root)
                e3.place(x=140, y=70)

                Button(root, text="Insert", command=insert, height = 1, width= 6).place(x=100, y=100)
                Button(root, text="Cancel", command=cancel, height = 1, width= 6).place(x=200, y=100)
            tab2()
    
        def cancel():
            root.destroy()

        def DELETE():   #deletes a record
            def tab3():
                def delete():
                    mysqldb = mysql.connector.connect(host='localhost',username='root',password='ASdf@2004',database='project')
                    my_cursor=mysqldb.cursor()
                    ename=e1.get()
    
                    sql = "delete from employee where emp_name = %s"
                    my_cursor.execute(sql, [(ename)])
    
                    mysqldb.commit()
                    print(my_cursor.rowcount, "record deleted")
                    messagebox.showinfo("","Record Deleted Successfully!")

                def cancel():
                    root.destroy()
    
                root = Tk()
                root.title("Delete")
                root.geometry("360x200")
                global e1

                Label(root, text="Employee Name").place(x=10, y=10)

                e1=Entry(root)
                e1.place(x=140, y=10)

                Button(root, text="Delete", command=delete, height = 1, width= 6).place(x=100, y=100)
                Button(root, text="Cancel", command=cancel, height = 1, width= 6).place(x=200, y=100)
            tab3()
            
        def DISPLAY():   #displays all the record
            def tab4():
                def table():
                    root = tk.Tk()
                    root.title("Details")
                    root.geometry("360x200")

                    mysqldb = mysql.connector.connect(host='localhost',username='root',password='ASdf@2004',database='project')
                    my_cursor=mysqldb.cursor()

                    my_cursor.execute("select * from employee")

                    tree=ttk.Treeview(root)

                    tree["columns"]=("empid","emp_name","emp_dept")

                    tree.column("empid", width=1, minwidth=30, anchor=tk.CENTER)
                    tree.column("emp_name", width=50, minwidth=100, anchor=tk.CENTER)
                    tree.column("emp_dept", width=50, minwidth=125, anchor=tk.CENTER)

                    tree.heading("empid",text="ID", anchor=tk.CENTER)
                    tree.heading("emp_name",text="Employee Name", anchor=tk.CENTER)
                    tree.heading("emp_dept",text="Employee Department", anchor=tk.CENTER)

                    i = 0
                    for r in my_cursor:
                        tree.insert('', i, text="", values=(r[0], r[1], r[2]))
                        i = i+1

                    tree.pack()
                table()
            tab4()

    
        root = Tk()
        root.title("Select Employee Option")
        root.geometry("360x200")

        Button(root, text="Add", command=ADD, height = 1, width= 10).place(x=150, y=10)
        Button(root, text="Delete", command=DELETE, height = 1, width= 10).place(x=150, y=40)
        Button(root, text="Display", command=DISPLAY, height = 1, width= 10).place(x=150, y=70)
        Button(root, text="Cancel", command=cancel, height = 1, width= 10).place(x=150, y=100)
    else:
        messagebox.showinfo("","Incorrect username and password")
        return False

def cancel():
    root.destroy()
    
root = Tk()
root.title("Login")
root.geometry("360x200")
global e1
global e2

Label(root, text="Username").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)

e1=Entry(root)
e1.place(x=140, y=10)

e2=Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")

Button(root, text="Login", command=Ok, height = 1, width= 6).place(x=100, y=100)
Button(root, text="Cancel", command=cancel, height = 1, width= 6).place(x=200, y=100)

root.mainloop()