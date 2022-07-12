from tkinter import *
import sqlite3

connect_ = sqlite3.connect("sujeet_1")
r = connect_.cursor()
class main_:
    def __init__(self, master):
        self.master = master
        self.master.title("police database")
        self.s= Frame(self.master, height= 600, width = 800)
        self.s.pack()
        self.s.propagate(0)
        create_sql = "CREATE TABLE IF NOT EXISTS police (Id REAL,Name TEXT,Salary  REAL, Cases_handled REAL)"
        r.execute(create_sql)
        self.e1 = Label(self.s, text="TABLE CREATED :Police", bg="white", font=('arial', 15))
        self.e2 = Entry(self.s, width=3, fg="black", bg="white", font=('arial', 15))
        self.e3 = Entry(self.s, width=10, fg="black", bg="white", font=('arial', 15))
        self.e4 = Entry(self.s, width=8, fg="black", bg="white", font=('arial', 15))
        self.e5 = Entry(self.s, width=3, fg="black", bg="white", font=('arial', 15))
        self.e6 = Entry(self.s, width=5, fg="black", bg="white", font=('arial', 15))
        self.e7 = Entry(self.s, width=10, fg="black", bg="white", font=('arial', 15))
        self.e8 = Entry(self.s, width=5, fg="black", bg="white", font=('arial', 15))
        self.e1.place(x=130, y=30)
        self.e2.place(x=50, y=110)
        self.e3.place(x=150, y=110)
        self.e4.place(x=330, y=110)
        self.e5.place(x=530, y=110)
        self.e6.place(x=50, y=190)
        self.e7.place(x=200, y=190)
        self.e8.place(x=50, y=270)
        self.l1 = Label(self.s ,text='CREATE TABLE')
        self.l2 = Label(self.s,text='Table Name :')
        self.l3 = Label(self.s,text='INSERT POLICEMEN RECORDS')
        self.l4 = Label(self.s,text='Id :')
        self.l5 = Label(self.s,text='Name :')
        self.l6 = Label(self.s,text='Salary :')
        self.l7 = Label(self.s,text='Cases_Handled :')
        self.l8 = Label(self.s,text='UPDATE POLICEMEN RECORDS')
        self.l9 = Label(self.s,text='Id :')
        self.l10 = Label(self.s,text='New Salary :')
        self.l11 = Label(self.s,text='DELETE RECORDS')
        self.l12 = Label(self.s,text='Id :')
        self.l13 = Label(self.s,text='DROP TABLE')
        self.l14 = Label(self.s,text='SHOW TABLE')

        self.val1 = StringVar()
        self.s1 = Spinbox(self.s, values=('Mumbai', 'Delhi', 'Kolkata', 'Chennai'), textvariable=self.val1, width=20, fg='black',
                     bg='gray',
                     font=('Arial', 12, 'bold italic'))

        self.var = IntVar()
        self.r1 = Radiobutton(self.s, text='MALE', variable=self.var, value=1)
        self.r2 = Radiobutton(self.s, text='FEMALE', variable=self.var, value=2)
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.c1 = Checkbutton(self.s, text='Java', variable=self.var1)
        self.c2 = Checkbutton(self.s, text='Python', variable=self.var2)
        self.c3 = Checkbutton(self.s, text='Databases', variable=self.var3)
        self.c4 = Checkbutton(self.s, text='Operating Systems', variable=self.var4)

        self.b2 = Button(self.s, text="INSERT RECORD", bg="white", font=('bold', 9), command=self.Insert)
        # b3 = Button(f, text="UPDATE SALARY", bg="gray", font=('bold', 10), command=display)
        # b4 = Button(f, text="DELETE", bg="gray", font=('bold', 10), command=display)
        # b5 = Button(f, text="DROP", bg="gray", font=('bold', 10), command=display)
        self.b6 = Button(self.s, text="SHOW", bg="gray", font=('bold', 10), command=self.display)

        self.l1.place(x=1, y=0)
        self.l2.place(x=20, y=30)
        self.l3.place(x=1, y=70)
        self.l4.place(x=20, y=110)
        self.l5.place(x=100, y=110)
        self.l6.place(x=280, y=110)
        self.l7.place(x=430, y=110)
        self.b2.place(x=580, y=110)
        self.l8.place(x=1, y=150)
        self.l9.place(x=20, y=190)
        self.l10.place(x=120, y=190)
        # b3.place(x=350, y=190)
        self.l11.place(x=1, y=230)
        self.l12.place(x=20, y=270)
        # 4.place(x=150, y=270)
        self.l13.place(x=1, y=350)
        self.l14.place(x=1, y=500)
        # b5.place(x=100, y=350)
        self.b6.place(x=100, y=500)

    def Insert(self):
        str1 = self.e2.get()
        str2 = self.e3.get()
        str3 = self.e4.get()
        str4 = self.e5.get()
        r.execute("INSERT INTO police VALUES (?,?,?,?)",(str1, str2, str3, str4))
        connect_.commit()
        b3=Button(self.s, text="next entry", command=self.Insert)
        b3.place(x=650,y =110)

    def exit_window(self):
        self.master.destroy()

    def display(self):
        root=Tk()
        self.frame= Frame(root, height=600, width= 800)
        self.frame.pack()
        show_="select * from police"
        r.execute(show_)
        self.rows_= r.fetchall()
        global i
        global j
        global k
        self.i=0
        self.j=50
        self.k=50
        while (1):
            self.l20=Label(self.frame, text=self.rows_[self.i])
            self.l20.place(x=self.j, y=self.k)
            self.i=self.i + 1
            self.k= self.k + 50


root = Tk()
root.title("LOG-IN")
f = Frame(root, height=400, width=400)
f.pack()
f.propagate(0)
def log():
    a = ex.get()
    b = ey.get()

    if (a == 'admin') and (b == 'admin'):
        l21=Label(f, text="successful")
        l21.place(x=300, y=300)
        root = Tk()
        sujeet = main_(root)
    else:
        l22=Label(f, text="invalid")
        l22.place(x=300, y=300)

lx = Label(f, text='User Name :')
ly = Label(f, text='Password :')
ex = Entry(f, width=5, fg='black', bg='gray', font=('arial', 20))
ey = Entry(f, width=5, fg='black', bg='gray', show='*', font=('arial', 20))
b = Button(f, text='Log-in',command=log)
b.place(x= 200, y=200)
lx.place(x=1, y=20)
ex.place(x=150, y=20)
ly.place(x=1, y=100)
ey.place(x=150, y=100)



root.mainloop()