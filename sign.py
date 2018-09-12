from tkinter import*
import tkinter.messagebox
def conf():
         #name = StringVar()
       # pas =StringVar()
        na = name.get()
        print ("New user:"+na)
        p = pas.get()
        a=0
        with open("User.txt","r+") as f:
              cont = f.readlines()
              for x in cont:
                      if na in x :
                            a=1                   
              if a!=1:
                f.write(na+'\n')
                f.close
                with open("Pass.txt","a") as g: 
                        g.write(p+'\n')
                        g.close
              else:
                tkinter.messagebox.showinfo("Error","Username already exits")
ro = Tk()
name = StringVar()
pas =StringVar()
ro.title("Sign Up")
#photo = PhotoImage(file="t.png")
#lab = Label(ro, image = photo).grid(row = 0, column = 1,sticky=W)
label= Label(ro,text="New Username:",width='20').grid(row = 1,column=0)
en = Entry(ro , textvariable = name,width='30').grid(row = 1,column=1,sticky=W)
label= Label(ro,text="New Password:",width='20').grid(row = 2,column=0)
en = Entry(ro , textvariable = pas,show='*',width='30').grid(row = 2,column=1,sticky=W)
but6 = Button(ro,text = "Confirm", command = conf).grid(row = 4,column=0)
but7 = Button(ro,text = "Cancel", command = quit).grid(row = 4,column=1)
ro.mainloop()
