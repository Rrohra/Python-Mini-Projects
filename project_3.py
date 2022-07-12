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

connect_ = sqlite3.connect("auction 2018_3")
r= connect_.cursor()

i =0
j=0


def create_():
    r.execute("CREATE TABLE IF NOT EXISTS Profile(SRno REAL,Name TEXT, Baseprice REAL, Team TEXT, Batting_attributes REAL, Bowling_attributes REAL)")
    connect_.commit()

def create_new():
    global i
    name = input("Enter the name of the player")
    baseprice = int(input("Input the baseprice of the new player"))
    bowling = int(input("Enter the bowling attributes"))
    batting = int(input("Enter the batting attributes"))
    s[i] = Player(name, baseprice, batting, bowling)
    s[i].insert_record

    i = i + 1


def print_records():
    global j
    insertsql = " select * from Profile where  Name = '%s'" % (s[j].name)
    r.execute(insertsql)
    attributes_ = r.fetchall()
    label1 = Label(right_frame, text=attributes_[0])
    label1.grid(row=3, column=0)
    j = j + 1

class Player:

    def __init__(self,n='', m='',o='',p=''):
        self.name= n
        self.team= 0
        self.baseprice=m
        self.batting_attributes=o
        self.bowling_attributes=p
    def insert_record(self):
        r.execute("insert into Profile(Name, Baseprice, Team, Batting_attributes, Bowling_attributes) VALUES (?,?,?,?,?)",
                  (self.name, self.baseprice, self.team, self.batting_attributes, self.bowling_attributes))
        connect_.commit()

s=[Player for i in range(30)]
create_()
new_entry=Button(rightmost_frame, text="New Player", command= create_new)
new_entry.pack()

next_button=Button(rightmost_frame, text="Next", command=print_records)
next_button.pack()



root.mainloop()