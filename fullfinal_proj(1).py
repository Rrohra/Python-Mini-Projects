from tkinter import *
from threading import *
import sqlite3
from PIL import Image,ImageTk

db = sqlite3.connect('test1.db')
cursor = db.cursor()


#mainwindow
class main_window:
    def __init__(self, master):
        self.master = master
        self.master.title("AUCTION")
        self.f = Frame(self.master, height = 1000,background='white', width = 1000)
        self.f.propagate(0)
        self.f.pack()

        self.photo_ = Image.open("auction4.jpg")  # image start
        self.photo_copy = self.photo_.copy()

        self.image_ = ImageTk.PhotoImage(self.photo_)

        self.l_p = Label(self.f, image=self.image_)
        self.l_p.bind('<Configure>', self._resize)
        self.l_p.pack(fill= BOTH, expand=YES)  # image end
        
        self.viewteam = Button(self.f, text = 'VIEW ITEMS',bg='white',activebackground= 'RosyBrown3', width = 25, command =self.view_teams,font='Helvetica')
        self.viewteam.place(x=100,y=600)

        self.exit = Button(self.f, text = 'EXIT', width = 25,bg='white',activebackground= 'RosyBrown3',command = self.exit_window, font='Helvetica')
        self.exit.place(x=700,y=600)

        self.auction = Button(self.f, text = 'AUCTION',bg='white', width = 25,activebackground= 'RosyBrown3',command = self.auction_window,font='Helvetica')        
        self.auction.place(x=400,y=600)

    def exit_window(self):
        self.master.destroy()

    def view_teams(self):
        self.view_teams = Toplevel(self.master)
        self.app = view_teams(self.view_teams)

    def auction_window(self):
        self.auction_window = Toplevel(self.master)
        self.auc = auctionwindow(self.auction_window)

    def _resize(self, event):
        self.n = event.width
        self.h = event.height
        self.photo = self.photo_copy.resize((self.n, self.h))

        self.image_ = ImageTk.PhotoImage(self.photo)
        self.l_p.configure(image=self.image_)


#Viewteamwindow    
class view_teams:
    def __init__(self, master):
        self.master = master
        self.master.title("AUCTION: ITEMS")
        self.f = Frame(self.master,height = 800,background='white', width = 1200)
        self.f.propagate(0)
        self.f.pack()

        self.photo_ = Image.open("soldout4.jpg")  # image start
        self.photo_copy = self.photo_.copy()

        self.image_ = ImageTk.PhotoImage(self.photo_)

        self.l_p = Label(self.f, image=self.image_)
        self.l_p.bind('<Configure>', self._resize)
        self.l_p.pack(fill=BOTH, expand=YES)  # image end

        self.exit = Button(self.f, text = 'EXIT',bg='white',activebackground= 'red', width = 25, command = self.exit_window)
        self.exit.place(x=500,y=600)
        cursor.execute("select * from anti")
        y=cursor.fetchall()
        self.l2=Label(self.master,bg='white',text="ID",width=20,font='arial 12')
        self.l2.place(x=150*1,y=50)
        self.l3=Label(self.master,bg='white',text="ANTIQUES",width=20,font='arial 12')
        self.l3.place(x=150*2,y=50)
        self.l4=Label(self.master,bg='white',text="DETAILS",width=20,font='arial 12')
        self.l4.place(x=150*3,y=50)
        self.l5=Label(self.master,bg='white',text="BUYER",width=20,font='arial 12')
        self.l5.place(x=150*4,y=50)
        self.l6=Label(self.master,bg='white',text="COST OF BIDDING",width=20,font='arial 12')
        self.l6.place(x=150*5,y=50)
        for r in range(0,len(y)):
            for c in range(0,5):
                self.l1=Label(self.master,bg='white',text=y[r][c],width=20,font='arial 9')
                self.l1.place(x=150*(c+1),y=100*(r+1))
        print(len(y))
        print(y)
        
    def exit_window(self):
        self.master.destroy()

    def _resize(self, event):
        self.n = event.width
        self.h = event.height
        self.photo = self.photo_copy.resize((self.n, self.h))

        self.image_ = ImageTk.PhotoImage(self.photo)
        self.l_p.configure(image=self.image_)


#Auction window
class pop:
    def __init__(self, master):
        self.master = master
        self.master.title("ERROR")
        self.f = Frame(self.master,background='white')
        self.f.propagate(0)
        self.f.pack()
        self.l11=Label(self.master,bg='red', text="FILL THE BLANK FIELDS",width=27)
        self.l11.pack()
        self.exit = Button(self.master, text = 'OK', width = 10,bg='white',activebackground= 'RosyBrown3',command = self.exit_window, font='arial 10')
        self.exit.pack(side='bottom')
    def exit_window(self):
        self.master.destroy()

class auctionwindow:

        
    def save(self):
        if(self.e1.get()=='' or self.e2.get()=='' or self.e3.get()=='' or self.e4.get()==''):
            self.aw = Toplevel(self.master)
            self.auc = pop(self.aw)
        else:
            
            self.l1=Label(self.master,bg='white', text=self.e1.get(),width=27)
            self.l1.place(x=50,y=100)
            self.l2=Label(self.master,bg='white', text=self.e2.get(),width=27)
            self.l2.place(x=50,y=200)
            self.l3=Label(self.master,bg='white', text=self.e3.get(),width=27)
            self.l3.place(x=50,y=300)
            self.l4=Label(self.master,bg='white', text=self.e4.get(),width=27)
            self.l4.place(x=50,y=400)
            
    def __init__(self, master):
        self.master = master
        self.master.title("AUCTION: AUCTION")
        self.f = Frame(self.master, height = 800,background='white', width = 1200)
        self.f.propagate(0)
        self.f.pack()

        self.photo_ = Image.open("white.jpg")  # image start
        self.photo_copy = self.photo_.copy()

        self.image_ = ImageTk.PhotoImage(self.photo_)

        self.l_p = Label(self.f, image=self.image_)
        self.l_p.bind('<Configure>', self._resize)
        self.l_p.pack(fill=BOTH, expand=YES)  # image end

        self.e1 = Entry(self.master,width=20,fg="black",font=('arial',12),bg="ghost white")
        self.e1.place(x=50, y=100)        
        self.b1 = Button(self.f, text = 'BID',bg='white',font = (24),activebackground= 'maroon',command = lambda: self.bidding(1))
        self.b1.place(x=300,y=100)
       
        self.e2 = Entry(self.master,width=20,fg="black",font=('arial',12),bg="ghost white")
        self.e2.place(x=50, y=200)
        self.b2 = Button(self.f, text = 'BID',font = (24),bg='white',activebackground= 'maroon',command = lambda: self.bidding(2))
        self.b2.place(x=300,y=200)

        self.e3 = Entry(self.master,width=20,fg="black",font=('arial',12),bg="ghost white")
        self.e3.place(x=50, y=300)
        self.b3 = Button(self.f, text = 'BID',font = (24),bg='white',activebackground= 'maroon',command = lambda: self.bidding(3))
        self.b3.place(x=300,y=300)

        self.e4 = Entry(self.master,width=20,fg="black",font=('arial',12),bg="ghost white")
        self.e4.place(x=50, y=400)
        self.b4 = Button(self.f, text = 'BID',font = (24),bg='white',activebackground= 'maroon',command = lambda: self.bidding(4))
        self.b4.place(x=300,y=400)

        
        
        self.exit = Button(self.f, text = 'EXIT',bg='white', width = 25,activebackground= 'maroon', command = self.exit_window)
        self.exit.place(x=700,y=500)

        self.b9=Button(self.f, text = 'SAVE',bg='white',activebackground= 'maroon',width=25,command=self.save)
        self.b9.place(x=350,y=500)
    
        
        #Player
        self.currbid = Label(self.master, text = 'Current Bidder :',bg='white',font = (24))
        self.currbid.place(x=400, y=100)
        
        self.name = Label(self.master, text = 'Item Name :',bg='white',font = (24))
        self.name.place(x=400, y=200)
                        
        self.cat = Label(self.master, text = 'Detail :',bg='white',font = (24))
        self.cat.place(x=400, y=300)

        #basevalue
        self.val = 2000
        
        self.bval = Label(self.master, text = 'Base value :',bg='white',font = (24))
        self.bval.place(x=400, y=400)  
        self.b_val = Label(self.master, text = '1000' ,bg='white', font = (24))
        self.b_val.place(x=600, y=400)
        
        
        #self.cval = Label(self.master, text = 'Current value :',font = (24))
        #self.cval.place(x=400, y=400)
        #self.c_val = Label(self.master, text = '1000',font = (24))
        #self.c_val.place(x=600, y=400)
        
        
        self.play = 1 
        if self.play == 1:
                cursor.execute("select * from anti where ID like {}".format(self.play))
                for r in cursor.fetchall():
                    print("antique name : {} {}".format(r[0],r[1]) )
                    antique_name = r[1]
                    self.playname = Label(self.master,bg='white', text = antique_name+"\t\t",font = (24))
                    self.playname.place(x=600, y=200)
                    self.details_=Label(self.master,bg='white', text=r[2], font=(24))
                    self.details_.place(x=600, y=300)
               
                self.image1=PhotoImage(file="db1.gif")
                self.l20=Label(self.master, image=self.image1)
                self.l20.place(x=900, y=100)
                print(self.play)



    def bidding(self,i):
        try:
            t = Timer(10.0, self.sold_to)
            t.start()
            if i == 1:
                self.name=self.l1.cget("text")
            elif i == 2:
                self.name=self.l2.cget("text")
            elif i == 3:
                self.name=self.l3.cget("text")
            elif i == 4:
                self.name=self.l4.cget("text")
                         
            self.val = self.val + 1000
            self.currbid = Label(self.master, text = self.name+"         ",bg='white',font = (24))
            self.currbid.place(x=600, y=100)
            
            self.cval = Label(self.master, text = 'Current value :',bg='white',font = (24))
            self.cval.place(x=400, y=450)  
            self.c_val = Label(self.master, text = self.val ,bg='white',font = (24))
            self.c_val.place(x=600, y=450)
        except AttributeError:
            t.cancel()
            self.a=Toplevel(self.master)
            self.auc=pop(self.a)

    def sold_to(self):
        try:
            print(self.name, self.val)
            self.sold = Label(self.master, text = 'Sold to :',bg='white',font = (24))
            self.sold.place(x=550, y=550)
            self.sold_t = Label(self.master, text = self.name ,bg='white',font = (24))
            self.sold_t.place(x=650, y=550)    
                
            self.next = Button(self.f, text = 'SAVE AND NEXT',bg='white',activebackground= 'tomato', width = 25,command = self.printrecord)
            self.next.place(x=520,y=700)
        except TypeError:
            self.a=Toplevel(self.master)
            self.auc=pop(self.a)
        
    def printrecord(self):
            cursor.execute("update anti SET sold_to= '{}',cost={} where ID like {} ".format(self.name,self.val,self.play))
            self.play=self.play+1
            db.commit()
            cursor.execute("select * from anti where ID like {}".format(self.play))
            self.val=1000
            for r in cursor.fetchall():
                print("Player name : {} {}".format(r[0],r[1]) )
                antique_name = r[1]
                self.playname = Label(self.master, text = antique_name+"\t\t",bg='white',font = (24))
                self.playname.place(x=600, y=200)
                self.details_=Label(self.master, text=r[2]+"\t",bg='white', font=(24))
                self.details_.place(x=600, y=300)
            self.sold = Label(self.master,bg='white', text = '\t',font = (16))
            self.sold.place(x=650, y=550)
            self.sold.config(font=("Courier", (24)))
            self.sold_t = Label(self.master, text = '\t' ,bg='white',font = (15))
            self.currbid = Label(self.master, text = '\t' ,bg='white',font = (24))
            self.c_val = Label(self.master, text = '\t' ,bg='white', font = (24))
            self.c_val.place(x=600, y=450)
            self.currbid.place(x=600, y=100)
            #self.sold_t.place(x=650, y=550)
            self.sold_t.config(font=("Courier", 24))
            if (self.play==2):
                self.image1=PhotoImage(file="db2.gif")
                self.l20=Label(self.master, image=self.image1)
                self.l20.place(x=900, y=100)
            elif (self.play==3):
                self.image1=PhotoImage(file="db4.gif")
                self.l20=Label(self.master, image=self.image1)
                self.l20.place(x=900, y=100)
            elif (self.play==4):
                self.image1=PhotoImage(file="db3.gif")
                self.l20=Label(self.master, image=self.image1)
                self.l20.place(x=900, y=100)
                

    def _resize(self, event):
        self.n = event.width
        self.h = event.height
        self.photo = self.photo_copy.resize((self.n, self.h))

        self.image_ = ImageTk.PhotoImage(self.photo)
        self.l_p.configure(image=self.image_)

    def exit_window(self):
        self.master.destroy()
root = Tk()
app = main_window(root)
root.mainloop()

