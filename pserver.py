

import socket 
from threading import Thread 
from socketserver import ThreadingMixIn 
from tkinter import *
from threading import *
import sqlite3
from PIL import Image,ImageTk

db = sqlite3.connect('test1.db', check_same_thread=False)
cursor = db.cursor()
a=1000

TCP_IP = '0.0.0.0' 
TCP_PORT = 2004 
play =2

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 
 
#mainwindow
class ClientThread(Thread):
    def __init__(self, master,ip,port):
        self.master = master
        self.master.title("AUCTION")
        self.f = Frame(self.master, height = 400,background='white', width = 400)
        self.f.propagate(0)
        self.f.pack()

        self.photo_ = Image.open("bgimage.jpg")  # image start
        self.photo_copy = self.photo_.copy()

        self.image_ = ImageTk.PhotoImage(self.photo_)

        self.l_p = Label(self.f, image=self.image_)
        self.l_p.bind('<Configure>', self._resize)
        self.l_p.pack(fill=BOTH, expand=YES)  # image end
        
        self.sold = Button(self.f, text = 'SOLD',activebackground= 'blue', width = 25,font='arial')
        self.sold.place(x=100,y=100)

        self.next= Button(self.f, text = 'NEXT', width = 25,activebackground= 'blue',font='arial', command=self.next_item)
        self.next.place(x=100,y=200)

        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print ("[+] New server socket thread started for " + ip + ":" + str(port))
        
       
    
    def run(self):
        self.data = conn.recv(2048)
        if self.data.decode() == 'start':
            cursor.execute("select * from anti where ID like 1")
            for r in cursor.fetchall():
                conn.send(r[1].encode())
                conn.send(r[2].encode())
        else:
            global a
            a= a+int(self.data.decode())
            self.l3=Label(self.master,text=a,width=20)
            self.l3.place(x=150*2,y=50)
            print ("Server received data:", self.data.decode())
    def _resize(self, event):
        self.n = event.width
        self.h = event.height
        self.photo = self.photo_copy.resize((self.n, self.h))

        self.image_ = ImageTk.PhotoImage(self.photo)
        self.l_p.configure(image=self.image_)
    def next_item(self):
        global play
        cursor.execute("select * from anti where ID like {}".format(play))
        for r in cursor.fetchall():
            conn.send(r[1].encode())
            conn.send(r[2].encode())
        play =play+1


# Multithreaded Python server : TCP Server Socket Program Stub


tcpServer.listen(4) 
print ("Multithreaded Python server : Waiting for connections from TCP clients...") 
root = Tk()
print('ssss')
(conn, (ip,port)) = tcpServer.accept()
newthread = ClientThread(root,ip,port)
print('aaaaaa')
newthread.start()
print('fffff')
threads.append(newthread)
print('jkhjk')
root.mainloop()
 
for t in threads: 
    t.join()

