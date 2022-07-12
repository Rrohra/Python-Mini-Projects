"""
this  functtion says hello
"""


def temp_conv(celsius):
    if celsius < -273.5:
        return "sorry"
    else:
        f = celsius * (9/5) +32
        return f
x= open("n", "w+")
temperatures= [10, -20, -289, 100]
for i in temperatures:
    z=temp_conv(i)
    print(type(z))
    if type(z)== float:
        y=x.write(str(z) + "\n")

x.close()