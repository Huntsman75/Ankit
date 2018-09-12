import mysql.connector
#import sys
conn = mysql.connector.connect(user='root', password='arvind', host= 'localhost')
import time
#from sign import *
from tkinter import *
import tkinter.messagebox
cursor = conn.cursor()
cursor.execute("USE Da")
#tday = datetime.date.today()
def show():
    cursor.execute("SELECT * FROM twitter")
    print ("            Date             Username        Tweet")
    for x in cursor.fetchall():
        print (x)
def intweet():
    r = Tk()
    no = time.asctime()
    #print(tday)
    #import mysql.connector
    #liconn = mysql.connector.connect(user='root', password='@rVindkumar.007', host= 'localhost')
    #cursor = conn.cursor()
    #cursor.execute("CREATE DATABASE Da")
    #cursor.execute("USE Da")
    #cursor.execute("CREATE TABLE twitter(date varchar(30),username varchar(50),tweet varchar(140))")
    b = input("Username:")
    c = input('Tweet:')
    cursor.execute("INSERT INTO twitter(date,username,tweet) VALUES(%s,%s,%s)",(no,b,c))
    conn.commit()
    tkinter.messagebox.showinfo("Insert!","Tweet has been posted!")
    #cursor.execute("ALTER FROM dat ADD COLUMN time time")
    print ("            Date             Username        Tweet")
    cursor.execute("SELECT *FROM twitter")
    for x in cursor.fetchall():
        print(x)

def deltweet():
    b = 0
    a = input("Whose tweet you want to delete:")
    cursor.execute("SELECT username FROM twitter")
    for x in cursor.fetchall():
        if a in x:
            cursor.execute("DELETE FROM twitter WHERE username=%s",(a,))
            conn.commit()
            cursor.execute("SELECT *FROM twitter")
            tkinter.messagebox.showinfo("Delete","Tweet has been deleted!")         
            print ("            Date             Username        Tweet")
            for x in cursor.fetchall():
                print(x)
            b = 1
    if b != 1: 
        print("Not Possible!")

def upmess():
    #tkinter.messagebox.showinfo("Update!,Do you want to update?")
    answer = tkinter.messagebox.askquestion("Update!","Do you want to update your tweet?")
    if answer == 'yes':
        uptweet()
        

def inmess():
    #tkinter.messagebox.showinfo("Update!,Do you want to update?")
    answer = tkinter.messagebox.askquestion("Insert!","Do you want to insert?")
    if answer == 'yes':
        intweet()
def delmess():
    #tkinter.messagebox.showinfo("Update!,Do you want to update?")
    answer = tkinter.messagebox.askquestion("Delete!","Do you want to delete your tweet?")
    if answer == 'yes':
        deltweet()

def uptweet():
    f = 0
    #b = input("Enter new tweet:")
    b = input("New Tweet:")
    a = input("Whose Tweet you want to update:")
    cursor.execute("SELECT username FROM twitter")
    for x in cursor.fetchall():
        if a in x:
            no = time.asctime()
            cursor.execute("UPDATE twitter SET tweet=%s, date=%s WHERE username=%s",(b,no,a))
            conn.commit()
            cursor.execute("SELECT * FROM twitter WHERE username=%s",(a,))
            print ("            Date             Username        Tweet")
            for x in cursor.fetchall():
                print(x)
            tkinter.messagebox.showinfo("Update!","Tweet has been updadted!")
            f = 1
        
    if f != 1: 
        print("Not Possible!")
def inp():
    z=0
    my = ment.get()
    pa = passw.get()
    if my == "":
                    tkinter.messagebox.showinfo("Error","You have to enter something")
    else:
        with open("User.txt") as f:
                user = f.readlines()
        with open("Pass.txt") as f:
                pas = f.readlines()
        for x in user:
            if my in x:
                for y in pas:
                    if pa in y:
            
            
                        #print ("true")
                        root = Tk()
                        root.title(" Twitter")
                        root.configure(background="yellow")
                        la = Label(root, text="Welcome!", bg = "yellow")
                        la.grid(row = 0, column = 2)
                        la1 = Label(root, text = "What you want to do?",bg = "yellow").grid(row = 1, column =2)
                        #frameone = Frame(root)
                        #frameone.pack(side=BOTTOM)
                        #bframe = Frame(root)
                        #bframe.pack(side=BOTTOM)
                        #ph = PhotoImage(file = "C:\\Python34\\twitter.png")
                        #label = Label(root, image = ph)
                        #lab.grid(row= 0, column = 1)
                        but2 = Button(root,text="Leave your Tweet",fg="blue",command=inmess)
                        but2.grid(row = 2, column = 1)
                        but1 = Button(root,text="Update your Tweet",fg="blue",command=upmess)
                        but1.grid(row= 2, column = 2)
                        but3 = Button(root,text="Delete your Tweet",fg="blue",command=delmess)
                        but3.grid(row = 2, column = 3)
                        but4 = Button(root,text="Quit",fg="red",command=quit)
                        but4.grid(row = 5 , column = 2)
                        but5 = Button(root,text="Show Tweets",command = show)
                        but5.grid(row = 4 , column = 2)
                        

                        root.mainloop()
                        z=1
                    
        if z!=1:
                tkinter.messagebox.showinfo(" Error","Invalid Username or Password!") 
# else if my == 'ankit' and pa == 'beautifulgame':
#    print ("true")
   # print ("false")
def imp():
    __import__('sign')



r = Tk()
r.geometry('300x300')
r.title("User Login")
la2 = Label(r, text="Login",).grid(row = 0, column = 1)
photo = PhotoImage(file = "C:\\Python34\\twitter.png")
label = Label(r, image = photo)
label.grid(row= 1, column = 1)
ment = StringVar()
passw = StringVar()
but = Button(r, text = "Sign In", command = inp)
but.grid(row = 8)
but = Button(r, text = "Exit", command = quit)
but.grid(row = 8, column = 2)
bu = Label(r, text="Username").grid(row = 2,column =0)
Entryn = Entry(r, textvariable = ment).grid(row = 2,column = 1)
la = Label(r, text = "Password").grid(row = 5,column = 0)
Ent = Entry(r, te = passw, show='*').grid(row = 5, column= 1)
but5 = Button(r, text = "Sign Up",command=imp).grid(row = 8, column = 1)
r.mainloop()


