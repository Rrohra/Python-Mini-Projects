from tkinter import *


def donothing():
    print("ohk boss")
root=Tk()

menu_rohit = Menu(root)
root.config(menu=menu_rohit)

submenu = Menu(menu_rohit)
menu_rohit.add_cascade(label="file", menu=submenu)  #to add drop down functionslity
submenu.add_command(label="new project..", command= donothing)
submenu.add_command(label="now", command = donothing)
submenu.add_separator()
submenu.add_command(label="exit", command =donothing)

submenu2= Menu(menu_rohit)
menu_rohit.add_cascade(label ="edit", menu=submenu2 )
submenu2.add_command(label="redo", command= donothing)



# ****************toolbar**************


toolbar= Frame(root, bg="blue")
insert_r= Button(toolbar, text="insert image", command=donothing)
insert_r.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side =TOP)


#***status box*****

status= Label(root, text="file saved", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
root.mainloop()
