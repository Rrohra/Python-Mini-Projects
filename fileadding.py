import datetime

name = datetime.datetime.now()
x= open("072 file1.txt", "r")
y= open("072 file2.txt", "r")
z= open("072 file3.txt", "r")
a =open(name.strftime('%Y-%M-%d'),"w+")


x1=x.read()
y1=y.read()
z1=z.read()

a1 = a.write(x1)
a1 = a.write(y1)
a1 = a.write(z1)

a.seek(0)
print(a.read())

x.close()
y.close()
z.close()
a.close()