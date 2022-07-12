from tkinter import *
import tkinter.messagebox

root=Tk()

tkinter.messagebox.showinfo('window Title',"kansha salvi")

answer= tkinter.messagebox.askquestion("question","do you like silly faces")

if answer == 'yes':
    print('silly faces')

root.mainloop()
