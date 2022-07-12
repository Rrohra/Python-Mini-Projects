from tkinter import *

root=Tk()
root.title("Details")
f=Frame(root,height=600, width=650)
f.propagate()
f.pack()

def display():
    str1 = e1.get()
    str2 = s1.get()
    str3 = e2.get()
    str4 = e3.get()
    x = var.get()
    x1 = var1.get()
    x2 = var2.get()
    x3 = var3.get()
    x4 = var4.get()
    str5 = ''
    str6 = ''
    if (x == 1):
        str5 += 'Your Gender is : Male'
    if (x == 2):
        str5 += 'Your Gender is : Female'
    if (x1 == 1):
        str6 += ' Java'
    if (x2 == 1):
        str6 += ' Python'
    if (x3 == 1):
        str6 += ' Database'
    if (x4 == 1):
        str6 += ' Operating System'
    l7 = Label(text='Your Name is : ' +str1, font=('Verdana', 10, 'italic bold'), fg='black').place(x=50, y=420)

    l8 = Label(text='Your City is : ' +str2, font=('Verdana', 10, 'italic bold'), fg='black').place(x=50, y=450)

    l9 = Label(text='Your Number is : ' +str3, font=('Verdana', 10, 'italic bold'), fg='black').place(x=50, y=480)

    l10 = Label(text='Your Age is : ' +str4, font=('Verdana', 10, 'italic bold'), fg='black').place(x=50, y=510)

    l11 = Label(text=str5, font=('Verdana', 10, 'italic bold'), fg='black').place(x=50, y=540)

    l12 = Label(text='Your Favourite Subject is : ' +str6, font=('Verdana', 10, 'italic bold'), fg='black').place(x=50, y=570)


l1 = Label(text='Enter your Name')
l2 = Label(text='Select your city')
l3 = Label(text='Enter your number')
l4 = Label(text='Enter your Age')
l5 = Label(text='Select your Gender')
l6 = Label(text='Favourite Subjects')
e1 = Entry(f, width=20, fg="black", bg="gray", font=('Arial', 15))

val1 = StringVar()
s1 = Spinbox(f, values=('Mumbai', 'Delhi', 'Kolkata', 'Chennai'), textvariable=val1, width=20, fg='black', bg='gray',
             font=('Arial', 12, 'bold italic'))

e2 = Entry(f, width=20, fg="black", bg="gray", font=('arial', 15))
e3 = Entry(f, width=20, fg="black", bg="gray", font=('arial', 15))
#e4 = Entry(f, width=20, fg="black", bg="gray", font=('arial', 15))


var = IntVar()
r1 = Radiobutton(f, text='MALE', variable=var, value=1)
r2 = Radiobutton(f, text='FEMALE', variable=var, value=2)
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
c1 = Checkbutton(f, text='Java', variable=var1)
c2 = Checkbutton(f, text='Python', variable=var2)
c3 = Checkbutton(f, text='Databases', variable=var3)
c4 = Checkbutton(f, text='Operating Systems', variable=var4)
b = Button(f, text="PRINT DETAILS", bg="gray", font=('bold', 11), command=display)

l1.place(x=50, y=30)
e1.place(x=200, y=30)
l2.place(x=50, y=60)
s1.place(x=200, y=60)
l3.place(x=50, y=90)
e2.place(x=200, y=90)
l4.place(x=50, y=120)
e3.place(x=200, y=120)
l5.place(x=50, y=180)
l6.place(x=50, y=220)
r1.place(x=190, y=180)
r2.place(x=260, y=180)
c1.place(x=190, y=220)
c2.place(x=190, y=250)
c3.place(x=190, y=280)
c4.place(x=190, y=310)
b.place(x=200, y=345)

root.mainloop()