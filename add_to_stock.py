from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
import tkinter.messagebox
from tkinter import messagebox
from tkinter import Text, Tk
import pymysql as p

con = p.connect(
    host='localhost',
    user='root',
    password='',
    db='gst'
    )
thirdw = Tk()

thirdw.title("GST BILLING SYSTEM")
thirdw.geometry("1750x1050+0+0")
label = Label(text="GST BILLING SYSTEM", font=("times new roman", 35), bg="MediumOrchid2")
label.pack(side=TOP, fill=X)

class rip():

    ##thirdw=Tk()
    ##thirdw.title("GST BILLING SYSTEM")
    ##thirdw.geometry("1750x1050+0+0")
    ##label=Label(text="GST BILLING SYSTEM",font=("times new roman",35),bg="MediumOrchid2")
    ##label.pack(side=TOP ,fill=X)
    ##print("fun1")
    def cat(self):
        print("hello everyone")

    def back(self):
        thirdw.destroy()
        import options
        options.options()
   

#print("got this far 1")


    def __init__(self,win):
        a=StringVar()
        b=StringVar()
        c=StringVar()
        e=StringVar()
        f=StringVar()
        g=StringVar()
        h=StringVar()
        self.l1 = Label(win, text="Product Name", font=("arial", 12))
        self.l1.place(x=470, y=139)
        self.e1 = Entry(width=10, bd=5, textvariable=a, font=("arial", 15))
        self.e1.place(x=750, y=139)
        self.l2 = Label(win, text="HSN Code", font=("arial", 12)).place(x=470, y=189)
        self.e2 = Entry(width=10, bd=5, textvariable=b,font=("arial", 15))
        self.e2.place(x=750, y=189)
        self.l3 = Label(win, text="Product Description", font=("arial", 12)).place(x=470, y=237)
        self.e3 = Entry(width=10, bd=5,textvariable=c, font=("arial", 15))
        self.e3.place(x=750, y=237)
        self.l4 = Label(win, text="Category", font=("arial", 12)).place(x=470, y=295)
        print("got this far 2")


        self.w=ttk.Combobox(win,textvariable=g,state="readonly",font=("arial",14))
        self.w['value']=('','Fashion','Grocery','Clothes','Electronics','Kids')
        
        self.w.current(0)
        self.w.place(x=750, y=295)
        print(self.w.current())
##        if self.w['value'] == 'Fashion':
##            result=18
##            self.e5.insert(END, str(result))
##        else:
##             self.e5.insert(END, 0)
        print("got this far 3")

        
        self.l5 = Label(win, text="Tax Type", font=("arial", 12)).place(x=470, y=351)
        self.e5 = Entry(width=10, bd=5,textvariable=e, font=("arial", 15))
        self.e5.place(x=750, y=351)
        self.l6 = Label(win, text="Price", font=("arial", 12)).place(x=470, y=380)
        self.e6 = Entry(width=10, bd=5,textvariable=f,font=("arial", 15))
        self.e6.place(x=750, y=380)
        self.l7 = Label(win, text="Quantity", font=("arial", 12)).place(x=470, y=440)
        self.e7 = Entry(width=10, bd=5,textvariable=h,font=("arial", 15))
        self.e7.place(x=750, y=440)
        print("got this far 4")
        cur = con.cursor()
        

        def add():
            tk.messagebox.showinfo('Add to Stock','Product added succesfully')
    
            a1=self.e1.get()
            b1=self.e2.get()
            c1=self.e3.get()
            g=self.w.get()
            k=self.e5.get()
            f1=self.e6.get()
            g1=self.e7.get()
            sql="""INSERT INTO `addition`(`p_name`, `hsn_code`, `p_description`,`category`,  `tax_type`, `price`,`quantity`) VALUES("%s","%s","%s","%s","%s","%s","%s")"""
            cur.execute(sql,(a1, b1, c1, g, k, f1,g1))
            if (cur.rowcount > 0):
                print("HEy")
                con.commit()
            else:
                print("BYE")
                con.rollback()
                con.close()
           
##        def ExitApplication():
##            MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
##            if MsgBox == 'yes':
##               thirdw.destroy()
##            else:
##                tk.messagebox.showinfo('Return','You will now return to the application screen')
##                
##        button1 = tk.Button (thirdw, text='Exit Application',command=ExitApplication)        

        print("got this far 5")
        self.b1 = Button(text="Add To Stock", width=26, font=("arial", 10), bg="indianred1", command=add).place(x=500,y=481)
        print("got this far 6")
        self.b2 = Button(text="Back To Options", width=26, font=("arial", 10), bg="indianred1", command=self.back).place(
        x=800, y=481)



print("fun1")
abc=rip(thirdw)
thirdw.mainloop()


#uic.18mca8027
