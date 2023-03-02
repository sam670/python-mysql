import os
import platform

ins = platform.system()
if ins=="Windows":
    os.system("pip install mysql-connector tk")
elif ins=="Linux":
    os.system("pip3 install mysql-connector tk")
else:
    pass

from tkinter import *
from tkinter.ttk import Progressbar
import mysql.connector as my
import csv
import datetime
from tkinter import messagebox
import time


base = Tk()  
base.geometry('500x500')
base.title("IMPORT CSV")
base.configure(bg='gray')

photo = PhotoImage(file = "samtech.png")
base.iconphoto(False, photo)

### All Labels

labl_0 = Label(base, text="Import Table Into CSV",width=20,font=("bold", 20),bg='gray')  
labl_0.place(x=80,y=20)  
  
labl_1 = Label(base, text="Host Name",width=20,font=("bold", 10),bg='gray')  
labl_1.place(x=80,y=90)  

labl_2 = Label(base, text="User Name",width=20,font=("bold", 10),bg='gray')  
labl_2.place(x=80,y=140)  

labl_3 = Label(base, text="Password",width=20,font=("bold", 10),bg='gray')  
labl_3.place(x=80,y=190)  

labl_4 = Label(base, text="Database Name",width=20,font=("bold", 10),bg='gray')  
labl_4.place(x=71,y=240)  

labl_5 = Label(base, text="Table Name",width=20,font=("bold", 10),bg='gray')  
labl_5.place(x=80,y=290)  


## the progressbar
progress = Progressbar(base, orient = HORIZONTAL,length = 100, mode = 'determinate')
if ins=="Windows":
    progress.place(x=70,y=340,width=315.)
elif ins=="Linux":
    progress.place(x=70,y=340,width=360.)
else:
    progress.place(x=70,y=340,width=360.)
#### All Entries

host2 = StringVar()
user2 = StringVar()
pass_2 = StringVar()
db2 = StringVar()
tb_name2 = StringVar()

host1 = Entry(base,textvariable=host2)  
host1.place(x=240,y=90)

user1 = Entry(base,textvariable=user2)  
user1.place(x=240,y=140)

pass_1 = Entry(base,textvariable=pass_2)  
pass_1.place(x=240,y=190)

db1= Entry(base,textvariable=db2)  
db1.place(x=240,y=240)

tb_name1 = Entry(base,textvariable=tb_name2)  
tb_name1.place(x=240,y=290)


## create_csv function is to create the csv file
def create_csv():
    try:
        host = host2.get()
        user = user2.get()
        pass_ = pass_2.get()
        db = db2.get()
        tb_name = tb_name2.get()
        
            
        if host=="":
            messagebox.showerror("Error","Please fill the host name")
        
        elif user=="":
            messagebox.showerror("Error","Please fill the user name")

        elif db=="":
            messagebox.showerror("Error","Please fill the Database name")
        
        elif tb_name=="":
            messagebox.showerror("Error","Please fill the Table name")
        

        currentDate = datetime.datetime.now().date()
        con = my.connect(user=user, passwd=pass_, host=host, db=db)
        cursor = con.cursor()
        
        ##### THIS IS THE QUERY YOU CAN EDIT HERE THE LIMITS AND ALL 
        ## EXAMPLE-- "select * from {}; limit 1000;".format(tb_name)

        query = "select * from {};".format(tb_name)
        cursor.execute(query)

        progress['value'] = 20
        base.update_idletasks()
        time.sleep(0.1)

        progress['value'] = 40
        base.update_idletasks()
        time.sleep(0.5)

        with open('table_Data_on_%s.csv' % currentDate, 'w') as f:
            writer = csv.writer(f)
            for row in cursor.fetchall():
                writer.writerow(row)

            progress['value'] = 80
            base.update_idletasks()
            time.sleep(0.1)
            if writer!=0:
                progress['value'] = 100
                messagebox.showinfo("Message",f'table csv file generated successfully..')
    except:
        pass


### clear function to clear all the UI data
def clear_data():
    host1.delete(0,END)
    user1.delete(0,END)
    pass_1.delete(0,END)
    db1.delete(0,END)
    tb_name1.delete(0,END)
    progress["value"] = 0

##Buttons
Button(base, text='Import CSV',width=20,bg='#363d4d',fg='white',command=lambda: [create_csv()]).place(x=70,y=400)  
Button(base, text='Clear',width=20,bg='#363d4d',fg='white',command=clear_data).place(x=240,y=400) 

# it will be used for displaying the registration form onto the window  
base.mainloop()
