# Python TCP Client A
import socket 
from tkinter import *
from PIL import Image,ImageTk


host = socket.gethostname()
print(host)
port = 2004


 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))

class main_window:
    def __init__(self, master):
        self.master = master
        self.master.title("AUCTION_client")
        self.f = Frame(self.master, height = 400,background='white', width = 400)
        self.f.propagate(0)
        self.f.pack()

        self.photo_ = Image.open("bgimage.jpg")  # image start
        self.photo_copy = self.photo_.copy()

        self.image_ = ImageTk.PhotoImage(self.photo_)

        self.l_p = Label(self.f, image=self.image_)
        self.l_p.bind('<Configure>', self._resize)
        self.l_p.pack(fill=BOTH, expand=YES)  # image end
        
        self.bid = Button(self.f, text = 'BID',activebackground= 'blue', width = 20,command=self.bid,font='arial')
        self.bid.place(x=100,y=220)

        self.current= Button(self.f, text = 'CURRENT VALUE', width = 20,activebackground= 'blue',font='arial')
        self.current.place(x=75,y=170)
        
        self.start= Button(self.f, text = 'START', width = 20,activebackground= 'blue',command=self.start,font='arial')
        self.start.place(x=100,y=20)

        self.l2= Label(self.f, text= 'current value:', width =20)
        self.l2.place(x=25, y=130)
    def run(self):
        data2 = tcpClientA.recv(2048)
        x=data2.decode()
        self.l7 = Label(self.f, text=x, width=30)
        self.l7.place(x=100, y=70)
        for Q in data2:

            #self.l2 = Label(self.f, text=Q[1], width=30)
            #self.l2.place(x=100, y=100)
            if (Q[1]=='SAMBHAJI SWORD'):
                self.image1 = PhotoImage(file="db2.gif")
                self.l4 = Label(self.f, image=self.image1)
                self.l4.place(x=50, y=100)
            elif (Q[1]=='CHAIR'):
                self.image1 = PhotoImage(file="db3.gif")
                self.l5 = Label(self.f, image=self.image1)
                self.l5.place(x=50, y=100)
            else:
                self.image1 = PhotoImage(file="db4.gif")
                self.l6 = Label(self.f, image=self.image1)
                self.l6.place(x=50, y=100)

    def start(self):
        self.MESSAGE='start'
        tcpClientA.send(self.MESSAGE.encode())
        data = tcpClientA.recv(1024)
        y=data.decode()
        self.l1= Label(self.f ,text= y,width=30 )
        self.l1.place(x=100, y=70)
        #self.l2=Label(self.f, text= r[1], width =30)
        #self.l2.place(x=100, y=100)
        #self.image1=PhotoImage(file="db1.gif")
        #self.l3=Label(self.f, image=self.image1)
        #self.l3.place(x=50, y=100)
        print (" Client received data:", data.decode())
               
    def bid(self):
        self.b='1000'
        tcpClientA.send(self.b.encode())
        self.data1=tcpClientA.recv(1024)
        self.l2= Label(self.f, text= self.data1.encode())
        self.l2.place(x=150, y=150)
        
    def _resize(self, event):
        self.n = event.width
        self.h = event.height
        self.photo = self.photo_copy.resize((self.n, self.h))

        self.image_ = ImageTk.PhotoImage(self.photo)
        self.l_p.configure(image=self.image_)


root = Tk()
app = main_window(root)
root.mainloop()
