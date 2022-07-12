'''a=45
h= oct(a)
h1= hex(a)
i =bin(a)
print (a,"", h,i, h1)

#k =input("whats ur name")
#print('your name is {}'.format(k))

print(type(a), type(h), type(i),type(h1))'''

#experitment 2

from array import *
'''x=[1,2,3,4,5,6,7,8,9,10,12,13,41,16,17] #list created
print(x)
x1= bytearray(x) #converted to bytearray
print(x1[0],x1[1],x1[2],x1[3],x1[4],x1[5],x1[6],x1[7],x1[10],x1[11],x1[13],x1[14],x1[9])
for i in range(0,15):
    print(x1[i])
r=list(range(11))
print(r)

s= {1,89,6,4,7,3,89}
print(s)
name= set('ROHRA')
print(name)
s1=s.update([1,100])
print(s1)

x= frozenset(s)
print(x)'''

'''str=("hello rohrA have a nice day coding")
print(str)
print(str[0:17])
print(str[-1])
print(str[8])
print(len(str))
print(str.count('a'))
print(str.replace('rohrA','rohit'))
print(sorted(str))

x=[1,2,3,4,5,'rohra',-1,2.309] #list
print(x)
for i in range(0,8):
    print(x[i])

print(x[0:4])
x.append('rohit')
print(x)
x1=[1,56,234,7,43,90,39455676,789,34556,36578]
print(x1)
x1.sort()
print(x1)'''

#factorial
'''x=int(input("ente3r the no. u wan to input"))
y= 1
while x!= 0 :
    y=y*x
    x= x-1
print(y)'''

#fibonacci
'''a=0
b=1
x= int(input("ebnter eht np."))
if x==1:
    print (a)
elif x==2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    while (x-2)!=0 :
        c=a+b
        a=b
        b=c
        print(c)
        x=x-1'''

#pascasl

'''n=int(input("Enter the rows:"))
a=[1]
y=[0]
for x in range(max(n,0)):
      print(a)
      a=[l+r for l,r in zip(a+y, y+a)]'''

''''#overriding and overloading
class Student:  # define parent class
    def __init__(self):
        print("Calling parent constructor")


    def teacher(self):  # Overridden Method (Method Over riding)
        print("Overriding Teacher method in Parent Class")


    def s_details(self):
        print(".........CALLING PARENT METHOD using Child Object......")
        self.roll = input("Enter Your Roll Number. -: ")
        self.name = input("Enter Your Name -: ")
        self.div = input("Enter Your Division -: ")
        self.city = input("Enter Your City -: ")
        print(" ")
        print("Student Details Are.....")
        print("Your Roll Number is", self.roll)
        print("Your Name is", self.name)
        print("Your Division is", self.div)
        print("Your City is", self.city)


    def sum(self, a=None, b=None, c=None):
        print(" ")

        print(".........METHOD OVERLOADING WITH a=10,b=20 and c=30......")

        if a is not None and b is not None and c is not None:
            print('Sum of a,b and c is', a + b + c)
        elif a is not None and b is not None:
            print('Sum of a and b is', a + b)
        else:
            print('Sum Not possible..Value of a is', a)


class College(Student):  # define child class (Inheritance)
    def __init__(self):
        print("Calling child constructor")

    def teacher(self):  # Overridden Method (Method Over riding)
        print(" ")
        print(".........METHOD OVERRIDING:Overriding Teacher method in Child Class")

    def c_details(self):
        print(".........CALLING CHILD METHOD using Child Object......")
        self.cname = input("Enter Your College Name -: ")
        self.uni = input("Enter Your University Name -: ")
        self.caddress = input("Enter Your College City  -: ")
        print(" ")
        print("Your College Details Are.....")
        print("Your College name is", self.cname)
        print("Your University is", self.uni)
        print("Your College City is", self.caddress)


c = College()  # instance of child
c.c_details()  # calls parent's method
c.s_details()  # calls parent's method
c.teacher()  # calls Overridden method
c.sum(10, 20, 30)  # Method overloading with three parameters
c.sum(10, 20)  # Method overloading with two parameters
c.sum(10)  # Method overloading with one parameters'''


'''class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x.Name())
print(y.GetEmployee())
print(y.Name())'''

#merhyo overloading

'''class operations:
    def product(self, a=0,b=0,c=0):
        if c==0 :
            self.x = a * b
            return self.x

        else:
            self.x= a*b*c
            return self.x



result=operations()
well=result.product(5,6)
print(well)
result2=operations()
well=result2.product(3,7,4)
print(well)'''

'''import os
ch=0
while(ch!=6):
	ch=int(input("Enter choice\n1:create file\n2:read file\n3:update file\n4:delete file\n5:count no.of words in file\n6:exit\n"))
	if(ch==1):
		n=input("Enter name of file\n")
		if(os.path.exists(n)):
			print("File already exists\n")
		else:
			f=open(n,"w")
			print("The file name is:\n",n)
			f.write(input("Enter contents to be written in file\n"))
			f.close()

	elif(ch==2):
		n=input("Enter name of file to be read\n")
		if(os.path.exists(n)):
			f=open(n,"r")
			print("The contents in file are:")
			for i in f:
				print(i)
			f.close()
		else:
			print("File does not exists")

	elif(ch==3):
		n=input("Enter name of file to be updated\n")
		if(os.path.exists(n)):
			f=open(n,"a")
			f.write(input( "Enter contents to be appended\n"))
			f.close()
		else:
			print("File does not exist\n")

	elif(ch==4):
		n=input("Enter name of file to deleted\n")
		if(os.path.exists(n)):
			os.remove(n)
			print("File deleted")
		else:
			print("File does not exist")

	elif(ch==5):
		c=0
		n=input("Enter name of file to be read\n")
		if(os.path.exists(n)):
			f=open(n,"r")
			for i in f:
				w=i.split()
				c+=len(w)
			print("Count of words are\n",c)
			f.close()
		else:
			print("File does not exist\n")

	elif(ch==6):

		exit(1)'''

'''from tkinter import *
root= Tk()
canvas_=Canvas(root, height= 100, width= 100)
canvas_.pack()

circle=canvas_.create_oval(25,25,75,75, fill='yellow')
triangle=canvas_.create_polygon(25,50,50,75,75,50, fill='green')
circle=canvas_.create_oval(37.5,50,62.5,75, fill='orange')


root.mainloop()'''



j=1
st = input("enter\n")
print("original string is ", st)
print("reversed string is", end=" ")
for i in st :
    print(st[-j], end="")
    j=j+1
