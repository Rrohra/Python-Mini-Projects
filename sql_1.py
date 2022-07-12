import sqlite3
import time
import random
from tkinter import *



connect_ = sqlite3.connect("auction 2018_1")
r= connect_.cursor()

# create a table

def create_():
    x= 'Profile1'
    r.execute("CREATE TABLE {}(Name TEXT, Status REAL, Baseprice REAL, Bat REAL, Bow REAL)".format(x))

def data():
    r.execute("INSERT INTO Profile1 VALUES('DivakarPandey',3466,0,88,59)")
    r.execute("INSERT INTO Profile1 VALUES('mohitpunjabi',4217,0,89,67)")
    r.execute("INSERT INTO Profile1 VALUES('MuskaanShaikh',     100000, 0,93,78)")
    r.execute("INSERT INTO Profile1 VALUES('AnirudhPoroorkara', 95000,  0,96,74)")
    r.execute("INSERT INTO Profile1 VALUES('SujeetPunjabi',     83000,  0,92,54)")
    r.execute("INSERT INTO Profile1 VALUES('JatinSachdev',      75000,  0,63,91)")
    r.execute("INSERT INTO Profile1 VALUES('SanaKhan',          43000,  0,75,89)")
    r.execute("INSERT INTO Profile1 VALUES('SirRajeev Punjabi', 10000,  0,43,43)")
    
    


'''def dynamic_entry():
    Baseprice= random.randrange(10000, 100000)
    Name = input("enter the name of the new player")
    Team =0
    Batting_attributes = int(input("enter the batting attributes of the new player"))
    Bowling_attributes = int(input("enter the bowling attributes of the new player"))
    r.execute("insert into Profile(Name, Baseprice, Team, Batting_attributes, Bowling_attributes) VALUES (?,?,?,?,?)",
              (Name, Baseprice, Team, Batting_attributes, Bowling_attributes))
    connect_.commit()
'''

data()
#dynamic_entry()
