import sqlite3
import time
import random
from tkinter import *
from array import *
import functools

root = Tk()
left_frame=Frame(root, width=100, height=100)
left_frame.pack(side='left')

right_frame=Frame(root,height= 100, width= 100)
right_frame.pack(side='left')

rightmost_frame=Frame(root,height= 100, width= 100)
rightmost_frame.pack(side='right')

connect_ = sqlite3.connect("auction_2018")
r= connect_.cursor()


def create_():
    r.execute("CREATE TABLE IF NOT EXISTS Profile(SRno REAL,Name TEXT, Baseprice REAL, Team TEXT, Batting_attributes REAL, Bowling_attributes REAL)")
    connect_.commit()
def entry_table():
    r.execute("INSERT INTO Profile VALUES(1,'Divakar Pandey',     34567,  0,88,59)")
    r.execute("INSERT INTO Profile VALUES(2,'mohit punjabi',      34217,  0,89,67)")
    r.execute("INSERT INTO Profile VALUES(3,'Muskaan Shaikh',     100000, 0,93,78)")
    r.execute("INSERT INTO Profile VALUES(4,'Anirudh Poroorkara', 95000,  0,96,74)")
    r.execute("INSERT INTO Profile VALUES(5,'Sujeet Punjabi',     83000,  0,92,54)")
    r.execute("INSERT INTO Profile VALUES(6,'Jatin Sachdev',      75000,  0,63,91)")
    r.execute("INSERT INTO Profile VALUES(7,'Sana Khan',          43000,  0,75,89)")
    r.execute("INSERT INTO Profile VALUES(8,'Sir Rajeev Punjabi', 10000,  0,43,43)")
    connect_.commit()

def print_records():
    r.execute("SELECT * FROM Profile Where Team=0")
    data1=r.fetchall()
    print(data1)


def print_attributes(event,a1):
    a = a1
    insertsql = " select * from Profile where  Name = '%s'" % (a1)
    r.execute(insertsql)
    attributes_ = r.fetchall()
    label1 = Label(right_frame, text=attributes_[0])
    label1.grid(row= 3,column=0)


create_()
entry_table()
r.execute("select name from Profile")
row_= r.fetchall()


button1=Button(rightmost_frame, text= row_[0],)
button1.bind("<Button-1>", functools.partial(print_attributes, a1=row_[0]))
button1.pack()
button2=Button(rightmost_frame, text= row_[1])
button2.bind("<Button-1>", functools.partial(print_attributes, a1=row_[1]))
button2.pack()
button3=Button(rightmost_frame, text= row_[2])
button3.bind("<Button-1>", functools.partial(print_attributes, a1=row_[2]))
button3.pack()
button4=Button(rightmost_frame, text= row_[3])
button4.bind("<Button-1>", functools.partial(print_attributes, a1=row_[3]))
button4.pack()
button5=Button(rightmost_frame, text= row_[4])
button5.bind("<Button-1>", functools.partial(print_attributes, a1=row_[4]))
button5.pack()
button6=Button(rightmost_frame, text= row_[5])
button6.bind("<Button-1>", functools.partial(print_attributes, a1=row_[5]))
button6.pack()
button7=Button(rightmost_frame, text= row_[6])
button7.bind("<Button-1>", functools.partial(print_attributes, a1=row_[6]))
button7.pack()
button8=Button(rightmost_frame, text= row_[7])
button8.bind("<Button-1>", functools.partial(print_attributes, a1=row_[7]))
button8.pack()



root.mainloop()




'''label1=Label(right_frame, text ="bid from team 1")
    label1.grid(row= 0, column=0)
    label2 = Label(right_frame, text="bid from team 2")
    label2.grid(row=1, column=0)
    label3 = Label(right_frame, text="bid from team 3")
    label3.grid(row=2, column=0)
    entry=Entry(right_frame)
    entry1=Entry(right_frame)
    entry2=Entry(right_frame)
    entry.grid(row=0, column=1)
    entry1.grid(row=1,column=1)
    entry2.grid(row=2, column=1)
'''