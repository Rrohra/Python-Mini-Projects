from tkinter import *
import sqlite3
import tkinter.messagebox

connect_ = sqlite3.connect("sujeet_1")
r = connect_.cursor()

root = Tk()
root.title("LOG-IN")
f = Frame(root, height=400, width=400, bg='black')
f.pack()
f.propagate(0)


def log():
    a = ex.get()
    b = ey.get()

    if (a == 'admin') and (b == 'admin'):
        l21 = Label(f, text="SUCCESSFUL", font=('arial', 10))
        l21.place(x=300, y=300)
        root = Tk()
        sujeet = MainClass(root)
    else:
        tkinter.messagebox.showinfo('INVALID', 'INVALID COMBINATION')


lx = Label(f, text='User Name :', font=('arial', 15), bg='black', fg='white')
ly = Label(f, text='Password :', font=('arial', 15), bg='black', fg='white')
ex = Entry(f, width=10, fg='white', bg='gray30', font=('arial', 15))
ey = Entry(f, width=10, fg='white', bg='gray30', show='*', font=('arial', 15))
b = Button(f, text='Log-in', command=log, font=('arial', 15), bg='deepskyblue3', fg='white')
b.place(x=200, y=200)
lx.place(x=1, y=20)
ex.place(x=150, y=20)
ly.place(x=1, y=100)
ey.place(x=150, y=100)


class MainClass:

    def __init__(self, master):
        self.master = master
        self.master.title("Select")
        self.s = Frame(self.master, height=600, width=600, bg='white')
        self.s.pack()
        self.s.propagate(0)
        create_sql = "CREATE TABLE IF NOT EXISTS police (Id REAL,Name TEXT,Salary  REAL, Cases_handled REAL)"
        r.execute(create_sql)
        self.b1 = Button(self.s, text='INSERT POLICEMEN RECORDS', bg='gray', font=('arial', 15), command=self.insert)
        self.b2 = Button(self.s, text='UPDATE POLICEMEN RECORDS', bg='gray', font=('arial', 15), command=self.update)
        self.b3 = Button(self.s, text='DELETE RECORDS', bg='gray', font=('gray', 15), command=self.deleter)
        self.b4 = Button(self.s, text='SHOW TABLE', bg='gray', font=('gray', 15), command=self.show)
        self.b5 = Button(self.s, text='DELETE TABLE', bg='gray', font=('gray', 15), command=self.drop)
        self.b1.place(x=70, y=10)
        self.b2.place(x=70, y=100)
        self.b3.place(x=70, y=200)
        self.b4.place(x=70, y=300)
        self.b5.place(x=70, y=400)

    def insert(self):
        self.root = Tk()
        self.root.title("Insert")
        self.i = Frame(self.root, height=400, width=400, bg='white')
        self.i.pack()
        self.i.propagate(0)

        self.l1 = Label(self.i, text='INSERT POLICEMEN RECORDS', bg='khaki')
        self.l2 = Label(self.i, text='Id :')
        self.l3 = Label(self.i, text='Name :')
        self.l4 = Label(self.i, text='Salary :')
        self.l5 = Label(self.i, text='Cases_Handled :')
        self.e1 = Entry(self.i, width=5, fg="black", bg="white", font=('arial', 12))
        self.e2 = Entry(self.i, width=20, fg="black", bg="white", font=('arial', 12))
        self.e3 = Entry(self.i, width=8, fg="black", bg="white", font=('arial', 12))
        self.e4 = Entry(self.i, width=5, fg="black", bg="white", font=('arial', 12))
        self.b1 = Button(self.i, text="INSERT RECORD", bg='black', fg="white", font=('bold', 12), command=self.insertt)

        self.l1.place(x=150, y=0)
        self.l2.place(x=5, y=50)
        self.l3.place(x=5, y=100)
        self.l4.place(x=5, y=150)
        self.l5.place(x=5, y=200)
        self.e1.place(x=100, y=50)
        self.e2.place(x=100, y=100)
        self.e3.place(x=100, y=150)
        self.e4.place(x=150, y=200)
        self.b1.place(x=160, y=290)
        #root.mainloop()

    def insertt(self):
        self.str1 = self.e1.get()
        self.str2 = self.e2.get()
        self.str3 = self.e3.get()
        self.str4 = self.e4.get()
        r.execute("INSERT INTO police VALUES (?,?,?,?)", (self.str1,self.str2, self.str3, self.str4))
        connect_.commit()

    def update(self):
        self.root = Tk()
        self.root.title("Update")
        self.u = Frame(self.root, height=500, width=500, bg='white')
        self.u.pack()
        self.u.propagate(0)

        self.l10 = Label(self.u, text='UPDATE POLICEMEN RECORDS', bg='white', font=('arial', 15))
        self.l6 = Label(self.u, text='Id :', font=('arial', 12))
        self.l7 = Label(self.u, text='New Salary :', font=('arial', 12))
        self.e5 = Entry(self.u, width=5, fg="black", bg="white", font=('arial', 12))
        self.e6 = Entry(self.u, width=8, fg="black", bg="white", font=('arial', 12))
        self.b1 = Button(self.u, text='UPDATE', bg='gray', font=('bold', 12),command=self.update1 )

        self.b1.place(x=100, y=250)
        self.l10.place(x=100, y=20)
        self.l6.place(x=5, y=100)
        self.l7.place(x=5, y=150)
        self.e5.place(x=100, y=100)
        self.e6.place(x=120, y=150)

    def update1(self):
        self.str1 = self.e5.get()
        self.str2 = self.e6.get()

        r.execute("UPDATE police SET Salary = ? WHERE Id = ?", (self.str2, self.str1))
        connect_.commit()


    def deleter(self):
        self.root = Tk()
        self.root.title("Delete Record")

        self.dr = Frame(self.root, height=350, width=500, bg='white')
        self.dr.pack()
        self.dr.propagate(0)
        self.l8 = Label(self.dr, text='DELETE RECORDS', bg='white', font=('bold', 15))
        self.l9 = Label(self.dr, text='Id :', font=('bold', 12))
        self.e7 = Entry(self.dr, width=5, fg="black", bg="white", font=('arial', 12))
        self.b1 = Button(self.dr, text='UPDATE', bg='gray', font=('bold', 12), command=self.delete1)

        self.l8.place(x=130, y=20)
        self.l9.place(x=20, y=100)
        self.e7.place(x=80, y=100)
        self.b1.place(x=100, y=200)

    def delete1(self):

        self.str11 = self.e7.get()
        r.execute("DELETE FROM police WHERE Id = ?", (self.str11,))
        connect_.commit()

    def show(self):
        self.root = Tk()
        self.root.title("Show Record")
        self.s = Frame(self.root, height=1000, width=500, bg='white')
        self.s.pack()
        self.s.propagate(0)
        self.x = "SELECT * FROM police"
        r.execute(self.x)
        y = r.fetchall()
        #global i
        #global j
        #global k
        #global l
        #i = 0
        #j = 50
        #k = 50


        for i in range(0, len(y)):
            for j in range(0, 4):
                self.l20 = Label(self.s, text=y[i][j], width=10)
                self.l20.place(x=50*(j + 1), y=50*(i + 1))
            #self.l20 = Label(self.s, text=self.y[i], font=('bold', 20))
            #self.l20.place(x=j, y=k)
            #i = i + 1
            #k = k + 50

    def drop(self):
        r.execute("DROP TABLE police")
        connect_.commit()

root.mainloop()