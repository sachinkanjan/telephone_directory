from tkinter import*
import sqlite3
import os
import csv
str="@gmail.com"
sqlite_file = 'C:/Users/sysadmin/Desktop/my_database.sqlite'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
if os.path.isfile(sqlite_file) == False:
     c.execute('CREATE TABLE contacts (contact_id integer PRIMARY KEY,f_name text NOT NULL,l_name text NOT NULL,email text NOT NULL UNIQUE,phone text NOT NULL UNIQUE)')

def delete():
     select=listbox.curselection()
     #print(select)
     delname=listbox.get(listbox.curselection()[0]) 
     #print("tuple is"+delname)
     # print("value is"+delname[0:3])
     index=select[0]
     listbox.delete(index)
     c.execute('SELECT * FROM contacts')
     c.execute('DELETE FROM contacts WHERE f_name = ?',(delname[0:6],))
     conn.commit()
     
     
     
def add():
    f_name = entry1.get()
    l_name = entry2.get()
    email = entry3.get()
    telephone = entry4.get()
    data_person_name = [(f_name,l_name,email,telephone)]
    c.executemany('INSERT INTO contacts(f_name, l_name,email,phone) VALUES (?,?,?,?)', data_person_name)
    for row in c.execute('SELECT * FROM contacts'):
        
        print(row)
    entry1.delete(0,last=25)
    entry2.delete(0,last=25)
    entry3.delete(0,last=25)
    entry4.delete(0,last=25)
    listbox.insert(END, f_name+' '+ l_name+ ': '+'    ' + email +'    '+ telephone)
    if f_name=="":
        labelError=Label(frame1, text="First Name is empty", fg="red")
        labelError.grid(columnspan=2)
    if l_name=="":
        labelError2=Label(frame1, text="Last Name is empty", fg="red")
        labelError2.grid(columnspan=2)
    if email=="":
        labelError3=Label(frame1, text="Email is empty", fg="red")
        labelError3.grid(columnspan=2)
    if(str not in email):
        labelError6=Label(frame1, text="Email is invalid", fg="red")
        labelError6.grid(columnspan=2)
 
 
    if telephone=="":
        labelError4=Label(frame1, text="Telephone is empty", fg="red")
        labelError4.grid(columnspan=2)
    if len(telephone)<10:
         
         labelError5=Label(frame1, text="phone no is invalid", fg="red")
         labelError5.grid(columnspan=2)
        
    conn.commit()

def save():
    listed=list(listbox.get(0,END))
    print(listed)
    f1=open("C:/Users/sysadmin/Desktop/output.txt","a")
    for line in listed:
        f1.write(line)
        f1.write("\n")
    f1.close()

def database():
    with open("C:/Users/sysadmin/Desktop/contact_database.txt", "w") as f:
        writer = csv.writer(f, delimiter='\t')
        cursor = c.execute("SELECT * FROM contacts")
        writer.writerow([i[0] for i in cursor.description])
        writer.writerows(cursor.fetchall())
    f.close()
    os.startfile("C:/Users/sysadmin/Desktop/contact_database.txt")

wn=Tk()
wn.geometry("1000x500")
wn.title("Telephone Directory")
wn.config(bg='powder blue')

frame1=Frame(wn)
frame2=Frame(wn)

frame1=Frame(wn,bg='powder blue')
frame2=Frame(wn,bg='powder blue')
frame1.pack()
frame2.pack()


label1=Label(frame1, text="List of contacts", font="Calibre 30",fg='blue',bg='powder blue')
label1.grid(row=0, columnspan=2)
label2=Label(frame1, text="First Name:", font="Calibre 18",bg='powder blue')
label2.grid(row=1, column=0,sticky='W')
label3=Label(frame1, text="Last Name:", font="Calibre 18",bg='powder blue')
label3.grid(row=2, column=0,sticky='W')
label4=Label(frame1, text="Email:", font="Calibre 18",bg='powder blue')
label4.grid(row=3, column=0,sticky='W')
label5=Label(frame1, text="Telephone:", font="Calibre 18",bg='powder blue')
label5.grid(row=4, column=0,sticky='W')

f_name=StringVar()
entry1=Entry(frame1,textvariable=f_name,width=25)
entry1.grid(row=1, column=1)
l_name=StringVar()
entry2=Entry(frame1,textvariable=l_name,width=25)
entry2.grid(row=2, column=1)
email=StringVar()
entry3=Entry(frame1,textvariable=email,width=25)
entry3.grid(row=3, column=1)
telephone=StringVar()
entry4=Entry(frame1,textvariable=telephone,width=25)
entry4.grid(row=4, column=1)
scrollbar=Scrollbar(frame2, orient=VERTICAL)
listbox=Listbox(frame2, selectmode=EXTENDED, yscrollcommand=scrollbar.set,width=80) 
listbox.grid(row=6, columnspan=15)
scrollbar.config(command=listbox)
button1=Button(frame2, text="Add", width=15, height=1, command=add)
button1.grid(row=5, column=0)
button2=Button(frame2, text="Delete",  width=15, height=1, command=delete)
button2.grid(row=5, column=1)
button3=Button(frame2, text="Save to file",  width=15, height=1, command=save)
button3.grid(row=5, column=2)
button4=Button(frame2, text="View Database",  width=15, height=1, command=database)
button4.grid(row=5, column=3)

wn.mainloop()
conn.close()

